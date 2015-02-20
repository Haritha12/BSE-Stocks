'''
Created on Dec 23, 2014

@author: Omair
'''

import errno
import csv
import urllib
import os
# import zipfile
from zipfile import ZipFile
import datetime
from datetime import date
# import solr
import pysolr
import operator
url = "http://www.bseindia.com/download/BhavCopy/Equity/" # EQ231214_CSV.ZIP
dir = "data2/"

a = date(2013, 1, 1)
b = date(2013, 5, 31)

print "Downloading files between "+a.isoformat()+" and "+b.isoformat()
delta = datetime.timedelta(days=1)  #Date Delta (increment) = 1 day
while a <= b:
    a += delta  #Increase a by one day
    try:
        if a.weekday() < 5: #ignore all weekends
            fileN = "EQ" + a.strftime("%d%m%y") + "_CSV.ZIP"
            zipfilepath = dir+"zips/"+fileN;
            if not os.path.exists(zipfilepath): # If file not already present
                print "Downloading:",a,'http://www.bseindia.com/download/BhavCopy/Equity/'+fileN
                urllib.urlretrieve('http://www.bseindia.com/download/BhavCopy/Equity/'+fileN, zipfilepath)
                ffile=open(zipfilepath,'rb')    #open and unzip the CSV inside
                zipping=ZipFile(ffile)
                for name in zipping.namelist():
                    output=dir+"output/"
                    zipping.extract(name,output)
                    ffile.close()
    except:
        continue
    
    
fileDir = os.getcwd()
fileNames=[]
for fileN in os.listdir(fileDir):
    if fileN.endswith(".csv"):
        fileNames.append(fileN)

for each in fileNames:
    cr = csv.reader(open(each,"rb"))
    firstline = True
    j=0
    for row in cr:
        if firstline:    #skip first line
            firstline = False
            continue
        if not os.path.exists("./data2/"+row[0]+".CSV"):
            f=open("E:./data/"+row[0]+".CSV", "a")
            c = csv.writer(f,lineterminator='\n')
            c.writerow(["Date","SC_CODE","SC_NAME","SC_GROUP","SC_TYPE","OPEN","HIGH","LOW","CLOSE","LAST","PREVCLOSE","NO_TRADES","NO_OF_SHRS","NET_TURNOV","TDCLOINDI"])
            row.insert(0,each[2:-4])
            c.writerow(row)
            f.close()
        else:
            f=open("./data2/" + row[0]+".CSV", "a")
            c = csv.writer(f,lineterminator='\n')
            row.insert(0,each[2:-4])
            c.writerow(row)
            f.close()

fileDir = os.getcwd()+"\\data2\\output"
print fileDir
fileNames=[]
for fileN in os.listdir(fileDir):
    if fileN.endswith(".CSV"):
        fileNames.append(fileDir+"\\"+fileN)
rate={}
for eachFile in fileNames:
       cr = csv.reader(open(eachFile,"rb"))
       firstline=True
       closelist=[]
       for row in cr:
              if firstline:    #skip first line
                     firstline = False
                     continue
              closelist.append(row[8])
       rate[eachFile.split("\\")[-1]]=(float(closelist[0])/float(closelist[-1]))-1

sorted_x = sorted(rate.items(), key=operator.itemgetter(1), reverse=True)[:10]
print sorted_x
         


"""print "Files gotten. Extracting CSV files from Zips"
fileDirectory=dir
fileNames=[]
for fileN in os.listdir(fileDirectory+"output/"):
    if fileN.endswith(".CSV"):
        fileNames.append(fileN)
        
 Delete everything from docs        
 http://localhost:8983/solr/collection1/update?stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E&commit=true

print "Indexing each file to Solr"
s = pysolr.Solr('http://localhost:8983/solr/collection1')   #Establish conn to Solr

 s.delete(q='*:*') # DELETE ALL records currently indexed 
i = 0
for eachfile in fileNames:
    reader = csv.DictReader(open(dir+"output/"+eachfile,"rb"))
    listOfAllRows = []
    for row in reader:
        row['SC_NAME'] = row['SC_NAME'].strip()
        d = datetime.datetime.strptime( eachfile[2:8], "%d%m%y" )  #Parse date
        row['id'] = str(row['SC_CODE']+d.isoformat()) # creating 'unique' id for each record(document) -> Company Code + Date
        row['DATE'] = str(d.isoformat()+'Z') # formatting date according to Solr format
        listOfAllRows.append(row)
    i = i+ len(listOfAllRows)
    s.add(listOfAllRows)    #Add all rows to Solr index
    print i,eachfile
s.optimize()
print "Indexing finished"""

            
            
