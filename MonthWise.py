import Tkinter as tk
from operator import itemgetter
import csv
import numpy as np
import pprint
from bs4 import BeautifulSoup
import urllib
import csv
import operator
import pylab as pl
import matplotlib.pyplot as plt
import plotly.plotly as py
from plotly.graph_objs import *

 



comp = []
bsenames = {}
sen = {}     
scores = {}    
 

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
    for code, name in bsenames.iteritems():
        if name == company:
            company = code
    correlate(company)
    
def correlate(comp):
    score = 0
    date = []
    out = []
    s2012 = {}
    s2013 = {}
    s2014 = {}
    sc2012 = {}
    sc2013 = {}
    sc2014 = {}
    prevb=0
    prevc=0    
    name="./data/files/"+comp+".csv"
    file = csv.reader(open(name,"rb"))
    next(file, None)
    count  =0
    for row1 in file:
        a = row1[0]
        split = a.split('-')
        if int(split[0]) == 2012:
            if split[1] in s2012.keys():
                s2012[split[1]] = float(s2012[split[1]])+ float(row1[6])   
                sc2012[split[1]] = sc2012[split[1]]+1             
            else:
                s2012[split[1]] = float(row1[6])
                sc2012[split[1]] = 1
        if int(split[0]) == 2013:
            if split[1] in s2013.keys():
                s2013[split[1]] = float(s2013[split[1]])+ float(row1[6])
                sc2013[split[1]] = sc2013[split[1]]+1                
            else:
                s2013[split[1]] = float(row1[6])
                sc2013[split[1]] = 1
        if int(split[0]) == 2014:
            if split[1] in s2014.keys():
                s2014[split[1]] = float(s2014[split[1]])+ float(row1[6]) 
                sc2014[split[1]] = sc2014[split[1]]+1               
            else:
                s2014[split[1]] = float(row1[6])
                sc2014[split[1]] = 1
                
    
    
    keys2 = sc2012.keys()
    for k in keys2:
        s2012[k] = s2012[k]/sc2012[k] 
    keys3 = sc2013.keys()
    for k in keys3:
        s2013[k] = s2013[k]/sc2013[k]  
    keys4 = sc2014.keys() 
    for k in keys4:
        s2014[k] = s2014[k]/sc2014[k]  
    
    
         
       
    v2012 = s2012.values()
    v2013 = s2013.values()
    v2014 = s2014.values()
    
    
    x= [1,2,3,4,5,6,7,8,9,10,11,12]
    plt.plot(x,v2012)
    plt.plot(x,v2013)
    plt.plot(x,v2014)
    plt.ylabel('Stock price')
    plt.xlabel('Month')
    plt.show()
    
    
    
    
    
    plt.figure(figsize=(7,7), dpi=100)

    groups = [v2012,v2013,v2014]
              
    group_labels = ["jan", "feb","mar", "apr","may", "jun","jul", "aug","sep", "oct","nov", "dec"]
    num_items = len(group_labels)
   
    ind = np.arange(num_items)
    
   
    margin = 0.01
    width = (2.-2.*margin)/num_items
    
    s = plt.subplot(1,1,1)
    for num, vals in enumerate(groups):
        print "plotting: ", vals
        # The position of the xdata must be calculated for each of the two data series
        xdata = ind+margin+(num*width)
        
        gene_rects = plt.bar(xdata, vals, width)    
   
    s.set_xticks(ind+0.5)
    s.set_xticklabels(group_labels)

    plt.show()
    
    
    
    
   
def loaddata():
    bse = csv.reader(open("./BigData/Sensex.csv","rb"))
    next(bse, None)
    names = csv.reader(open("./BigData/BSE100.csv","rb"))
    for na in names:
        bsenames[na[0]] = na[1]
        comp.append(na[0])
    for r in bse:
        sen[r[0]] = r[4]
    

def correlation():
    count = 0
    for row in comp:
        score = 0
        prevb=0
        prevc=0
        count =count+1
        
        name="./data/files/"+row+".csv"
        file = csv.reader(open(name,"rb"))
        next(file, None)
        for row1 in file:
            temp = row1[0]
            if prevb == 0:
                prevb = sen[temp]
                prevc = row1[6]
            else:
                if temp in sen.keys():
                    x = sen[temp]
                    y = row1[6]
                    diffb = float(x) - float(prevb)
                    diffc = float(y) - float(prevc)
                    if diffb>0 and diffc>0:
                        score = score+1
                    elif diffb>0 and diffc<0:
                        score = score-1
                    elif diffb<0 and diffc>0:
                        score = score+2
                    
                    
                    prevb = x
                    prevc = y
            #print row[0],score
            
        #print row[0]+"==============="+str(score)
        scores[bsenames[row]] = score
    
    sorted_scores = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)

    for a in sorted_scores:
        print a







def main():
    loaddata()
    #correlation()
    display()
    
   


if __name__ == "__main__":
    main()