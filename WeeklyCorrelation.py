import Tkinter as tk

import csv
import numpy as np

from bs4 import BeautifulSoup
import urllib
import csv
import datetime
import matplotlib.pyplot as plt



 

meanstds = []

comp = []
bsenames = {}
sen = {}     
scores = {}    
dates = [] 

root = tk.Tk()
var = tk.StringVar(root) 


def display():
    
    root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
    root.title("Select company")
    choices = comp
    
    # initial value
    var.set('select')
    option = tk.OptionMenu(root, var, *choices)
    option.pack(side='left', padx=10, pady=10)    
    button = tk.Button(root, text="OK", command=ok)
    button.pack(side='left', padx=10, pady=10)        
    root.mainloop()

def ok():
    company = var.get()
    weeklyCorrelation(company)

def forall():
    
    for c in comp:
        weeklyCorrelation(c)
    b = open('./BigData/mean.csv', 'wb')
    a = csv.writer(b)
    
    a.writerows(meanstds)
    b.close()
            


def weeklyCorrelation(company):
    
    print company,"======================"
    corr = []
    meanstd = []
    comp = company        
    name="./BigData/files/"+comp+".csv"
    file = csv.reader(open(name,"rb"))
    next(file, None)
    weekav = {}
    weekaverages = {}
    weekaverages1 = {}
    count  =0
    weeks  =0
    weekday = 0
    sum = 0
    year = 0
    days =0
    y = 0
    y1 = 0
    for row in file:
        s1 = str(row[0]).split('-')
        
        s= datetime.datetime(int(s1[0]),int(s1[1]),int(s1[2]))
        if s1[0] == "2014": 
            
            if count == 0:
                count = 1
                weekday = s.isoweekday()
                
                sum = float(row[6])
                days+=1
                
            else:
                if weekday >= s.isoweekday():
                    #print weekday,s.isoweekday()
                    sum = sum + float(row[6])
                    days+=1
                    weekday = s.isoweekday()
                    #print sum
                else:
                    weeks = weeks+1
                    weekaverages[weeks] = sum/days
                    days = 0
                    #print str(weekday)+" "+str(s.isoweekday())+"=========="
                    sum = float(row[6])
                    weekday = s.isoweekday()  
        if int(s1[0]) < 2014:
            #print s1,y
            #print days
            if y != s1[0]:
                #print "xxxx   "+str(y)
                weekav[y] = weekaverages1
                y = s1[0]
                year = 0
                weeks = 0
                weekaverages1 = {}
            
            if year == 0:
                days = 0
                weekday = s.isoweekday()
                sum = float(row[6])
                days = days+1
                year = 1
            else:
                if weekday >= s.isoweekday():
                    #print weekday,s.isoweekday()
                    sum = sum + float(row[6])
                    days+=1
                    weekday = s.isoweekday()
                    #print sum
                else:
                    weeks = weeks+1
                    if days>0:
                        weekaverages1[weeks] = sum/days
                    days = 0
                    #print str(weekday)+" "+str(s.isoweekday())+"=========="
                    sum = float(row[6])
                    weekday = s.isoweekday() 
                
            
    weekav[y] = weekaverages1   
    y2014 =  weekaverages.values()
    a1 =  weekav["2013"]
    y20131 = a1.values()
    if len(y2014)==52 and len(y20131)==52:
        print "Correlation between 2014&2013", np.corrcoef(y2014,y20131)[0][1]
        corr.append(np.corrcoef(y2014,y20131)[0][1])
    
    years = ["2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000",]
    
    y1 = 2013
    while str(y1-1) in weekav.keys():
            
        a =  weekav[str(y1)]
        y2013 = a.values()
        b = weekav[str(y1-1)]
        y2012 = b.values()
        #print y2014
        #print y2013
        #print len(y2012),len(y2013)
        if len(y2012)==52 and len(y2013)==52:
        
            print "Correlation between "+str(y1-1)+ "&"+ str(y1), np.corrcoef(y2012,y2013)[0][1]
            corr.append(np.corrcoef(y2012,y2013)[0][1])
        #print "Correlation between 2013 & 2014", np.corrcoef(y2013,y2014)[0][1]
            x= range(1, 53)
            
            p2013, = plt.plot(x,y2013,label='2013')
            p2012, = plt.plot(x,y2012, label='2012')
            plt.legend([p2013, p2012], [str(y1), str(y1-1)])
            plt.ylabel('Week average of Stock price')
            plt.xlabel('Weeks')
            plt.title(str(y1)+"vs"+ str(y1-1)) 
            #plt.show()
        elif len(y2012)>=51 and len(y2013)>=51:
        
            print "Correlation between "+str(y1-1)+ "&"+ str(y1), np.corrcoef(y2012[:51],y2013[:51])[0][1]
        #print "Correlation between 2013 & 2014", np.corrcoef(y2013,y2014)[0][1]
            corr.append(np.corrcoef(y2012[:51],y2013[:51])[0][1])
            x= range(1, 52)
            
            p2013, = plt.plot(x,y2013[:51])
            p2012, = plt.plot(x,y2012[:51])
            plt.legend([p2013, p2012], [str(y1), str(y1-1)])
            plt.ylabel('Week average of Stock price')
            plt.xlabel('Weeks')
            plt.title(str(y1)+"vs"+ str(y1-1)) 
            #plt.show()
        y1 = y1-1
        
    print np.mean(corr)
    print np.std(corr)
    meanstd.append(company)
    meanstd.append(np.mean(corr))
    meanstd.append(np.std(corr))
    meanstd.append(y1+1)
    meanstds.append(meanstd)
        
       
        
       
    
    
    
    
    
    
def loaddata():
    bse = csv.reader(open("./BigData/Sensex.csv","rb"))
    next(bse, None)
    names = csv.reader(open("./BigData/bsenames.csv","rb"))
    for na in names:
        bsenames[na[0]] = na[1]
        comp.append(na[0])
    for r in bse:
        sen[r[0]] = r[6]
        #print str(r[0])
        
        #print dat
       
        #print s.isoweekday()
        
        
    


def main():
    loaddata()
    forall()
    #display()
    #weeklyCorrelation()
    #loaddata()
    
    #display()
    
   


if __name__ == "__main__":
    main()