from operator import itemgetter
import csv
import numpy as np
import pprint


from bs4 import BeautifulSoup

import urllib
import csv
import operator



comp = []
bse = csv.reader(open("./data/Sensex.csv","rb"))
next(bse, None)

names = csv.reader(open("./data/bsenames.csv","rb"))

bsenames = {}
for na in names:
    bsenames[na[0]] = na[1]
    comp.append(na[0])
    

sen = {}

for r in bse:
    sen[r[0]] = r[6]
    
scores = {}    
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
            
            
            
            
            
            
    