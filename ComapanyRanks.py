import Tkinter as tk

import csv
import numpy as np

from bs4 import BeautifulSoup
import urllib
import csv
import datetime
import matplotlib.pyplot as plt
from datetime import date, timedelta
import operator

monthweights = {}
yearweights = {}
weekweights = {}

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
    names = bsenames.values()
    choices = names
    
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
            


def weeklyrank():
    
    weekchangeavgs = {}
    
    for company in comp:       
        
        #print company,"======================"  
             
        compn = company        
        name="./BigData/files/"+compn+".csv"
        file = csv.reader(open(name,"rb"))
        next(file, None)    
        weekchange = {}    
        count  =0
        weeks  =0
        weekday = 0
        sum = 0    
        days =0
        
        sdate = "1/1/14"
        start_date = datetime.datetime.strptime(sdate, "%m/%d/%y").date()
        s1 = sdate.split('/')
        
        
        end_date = datetime.datetime.strptime(s1[0]+"/"+s1[1]+"/"+str(int(s1[2])+1), "%m/%d/%y").date()- timedelta(days=1)
        #print start_date
        #print end_date

        #print s1[0]
        
        
        for row in file:   
            
            date = datetime.datetime.strptime(row[0], '%d-%B-%Y').date()
                             
            if date<=end_date:         
                
                if count == 0:
                    count = 1
                    weekday = date.isoweekday()
                    
                    week_end = float(row[4])
                    days+=1
                    
                else:
                    if weekday >= date.isoweekday():
                       
                        week_start = float(row[4])
                        days+=1
                        weekday = date.isoweekday()                    
                        
                        #print sum
                    else:
                        weeks = weeks+1
                        weekchange[weeks] = ((week_end-week_start)/week_start)*100
                        days = 0
                        #print str(weekday)+" "+str(s.isoweekday())+"=========="
                        week_end = float(row[4])
                        weekday = date.isoweekday()  
                        
            if date<=start_date:
                if days != 0:
                    weeks = weeks+1
                    weekchange[weeks] = ((week_end-week_start)/week_start)*100               
                break
        
        #print company,weekchange
        avg = np.mean(weekchange.values())
        
        #print avg
        weekchangeavgs[company] = avg   
        #changes = weekchange
    sorted_avgs = sorted(weekchangeavgs.items(), key=operator.itemgetter(1),reverse=True)
   
    cnt = 99
    for a in sorted_avgs:
        
       
        weekweights[a[0]] = float(cnt)/100
        #print str(cnt)+")"+bsenames[a[0]]+"========"+str(a[1])
        cnt -=1        
   
    sorted_week_weights = sorted(weekweights.items(), key=operator.itemgetter(1),reverse=True)
    
   
                
       
def monthlyrank():  
         
    monthchangeavgs = {}
    
    for company in comp:       
        
        #print company,"======================"  
             
        compn = company        
        name="./BigData/files/"+compn+".csv"
        file = csv.reader(open(name,"rb"))
        next(file, None)    
        monthchange = {}    
        count  =0
         
        days =0
        
        sdate = "1/1/14"
        start_date = datetime.datetime.strptime(sdate, "%m/%d/%y").date()
        s1 = sdate.split('/')
        
        
        end_date = datetime.datetime.strptime(s1[0]+"/"+s1[1]+"/"+str(int(s1[2])+1), "%m/%d/%y").date()- timedelta(days=1)
        
        start_val = 0
        end_val = 0
        month = 0
        
        for row in file:   
            
            date = datetime.datetime.strptime(row[0], '%d-%B-%Y').date()
            if date<=end_date:
                          
                if month==0:
                    month = date.strftime('%m')
                    end_val = float(row[4])
                    start_val = float(row[4])
                else:
                    if month == date.strftime('%m'):
                        start_val =  float(row[4])
                    else:
                        if date <= start_date:
                            monthchange[month] = ((start_val-end_val)/start_val)*100      
                            #print start_val-end_val                
                            break
                        else:
                            monthchange[month] = ((start_val-end_val)/start_val)*100 
                            #print start_val-end_val 
                            end_val = float(row[4])     
                            month = date.strftime('%m')       
                        
            
        
        #print company,weekchange
        avg = np.mean(monthchange.values())
        
        #print avg
        monthchangeavgs[company] = avg   
        #changes = weekchange
    sorted_avgs = sorted(monthchangeavgs.items(), key=operator.itemgetter(1),reverse=True)
   
    cnt = 99
    for a in sorted_avgs:
        
       
        monthweights[a[0]] = float(cnt)/100
       
        cnt -=1        
   
    sorted_month_weights = sorted(monthweights.items(), key=operator.itemgetter(1),reverse=True)
    
    
    
    
def yearlyrank():
    
    yearchanges = {}
    for company in comp:       
        
        #print company,"======================"  
             
        compn = company        
        name="./BigData/files/"+compn+".csv"
        file = csv.reader(open(name,"rb"))
        next(file, None)    
            
        count  =0
         
        days =0
        
        sdate = "1/1/14"
        start_date = datetime.datetime.strptime(sdate, "%m/%d/%y").date()
        s1 = sdate.split('/')
        
        
        end_date = datetime.datetime.strptime(s1[0]+"/"+s1[1]+"/"+str(int(s1[2])+1), "%m/%d/%y").date()- timedelta(days=1)
        
        start_val = 0
        end_val = 0
        
        count = 0
        for row in file:   
            
            date = datetime.datetime.strptime(row[0], '%d-%B-%Y').date()
            if date<=end_date:
                if count == 0:
                    end_val = float(row[4])
                    start_val = float(row[4])
                    count = 1
                else:
                    if date<=start_date:
                        break
                    else:
                        start_val = float(row[4])
                    
        change = ((start_val-end_val)/start_val)*100 
                     
        #print change             
       
        yearchanges[company] = change  
        
    sorted_avgs = sorted(yearchanges.items(), key=operator.itemgetter(1),reverse=True)
   
    cnt = 99
    for a in sorted_avgs:
        
       
        yearweights[a[0]] = float(cnt)/100
       
        cnt -=1        
   
    sorted_year_weights = sorted(yearweights.items(), key=operator.itemgetter(1),reverse=True)
    
    
    
def calculateweight():
    weights = {}
    for company in comp:
        weights[company] = monthweights[company]+weekweights[company]+yearweights[company] 
         
    final_weights = sorted(weights.items(), key=operator.itemgetter(1),reverse=True)
    
    print "Final weights are"
    
    for a in final_weights:        
        print str(bsenames[a[0]])+"-------->"+str(a[1]) 
    
    
def loaddata():
    bse = csv.reader(open("./NewData/Sensex.csv","rb"))
    next(bse, None)
    names = csv.reader(open("./NewData/BSE100.csv","rb"))
    for na in names:
        bsenames[na[0]] = na[1]
        comp.append(na[0])
    for r in bse:
        sen[r[0]] = r[4]
        
        
    


def main():
    loaddata()
    weeklyrank()
    monthlyrank()
    yearlyrank()
    calculateweight()
    
    
   


if __name__ == "__main__":
    main()