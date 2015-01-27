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


comp = []
bsenames = {}
sen = {}    
scores = {}    
 

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
    correlate(company)
    
def correlate(comp):
    score = 0
    date = []
    out = []
    prevb=0
    prevc=0
    
    name="./data/files/"+comp+".csv"
    file = csv.reader(open(name,"rb"))
    next(file, None)
    count  =0
    for row1 in file:
        if count < 30:
            val = 0
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
                        val = 1
                    elif diffb>0 and diffc<0:
                        val = -1
                    elif diffb<0 and diffc>0:
                        val = 2
                    elif diffb<0 and diffc<0:
                        val = 0
                        
                        
                    prevb = x
                    prevc = y
                #print row[0],score
            print count
            count = count+1
            date.append(temp)
            out.append(val)
            
        #print row[0]+"==============="+str(score)
    print date
    print out
    
    fig = pl.figure()
    ax = pl.subplot(111)
    ax.bar(range(len(date)), out)
    width=0.8
    ax.set_xticks(np.arange(len(date)) + width/2)
    #ax.set_xticklabels(date, rotation=90)
    
    pl.show()
    
       
    
    
    
def loaddata():
    bse = csv.reader(open("./data/Sensex.csv","rb"))
    next(bse, None)
    names = csv.reader(open("./data/bsenames.csv","rb"))
    for na in names:
        bsenames[na[0]] = na[1]
        comp.append(na[0])
    for r in bse:
        sen[r[0]] = r[6]
    

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
    correlation()
    display()
    #display()
   


if __name__ == "__main__":
    main()