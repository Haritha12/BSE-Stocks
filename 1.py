import errno
import os
import urllib
import zipfile
import csv
import operator

f1="EQ"
f3="1014_CSV.ZIP"
f2=0

for i in range(1,31):
       try:
           if f2>=9:
               f2=f2+1;
               fileN=f1+`f2`+f3
           else:
               f2=f2+1
               fileN = f1+'0'+`f2`+f3
           filename = os.path.join("E:/Modules/DADV", fileN)
           if not os.path.exists(filename):
               urllib.urlretrieve('http://www.bseindia.com/download/BhavCopy/Equity/'+fileN, fileN)
           fh = open(fileN, 'rb')
           z = zipfile.ZipFile(fh)
           for name in z.namelist():
               outpath = "E:/Modules/DADV"
               z.extract(name, outpath)
               fh.close()
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
        if not os.path.exists("E:/Modules/DADV/output/"+row[0]+".CSV"):
            f=open("E:/Modules/DADV/output/"+row[0]+".CSV", "a")
            c = csv.writer(f,lineterminator='\n')
            c.writerow(["Date","SC_CODE","SC_NAME","SC_GROUP","SC_TYPE","OPEN","HIGH","LOW","CLOSE","LAST","PREVCLOSE","NO_TRADES","NO_OF_SHRS","NET_TURNOV","TDCLOINDI"])
            row.insert(0,each[2:-4])
            c.writerow(row)
            f.close()
        else:
            f=open("E:/Modules/DADV/output/" + row[0]+".CSV", "a")
            c = csv.writer(f,lineterminator='\n')
            row.insert(0,each[2:-4])
            c.writerow(row)
            f.close()

fileDir = os.getcwd()+"\\output"
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
         
