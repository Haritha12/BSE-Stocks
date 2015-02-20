import csv
import pprint
import urllib
import csv
import operator
 

CODE_LIST = []
BSE_CODE_NAMES = {}  

yRank = {}

#function loads all files
def loadData():
    
    names = csv.reader(open("./BigData/BSE100.csv","rb"))
    
    for na in names:
        BSE_CODE_NAMES[na[0]] = na[1]
        CODE_LIST.append(na[0])
    
    #print BSE_CODE_NAMES
             
def yearWise():
    
    #print CODE_LIST
    lastCp = {}
    firstCp = {}
    gainper = {}
    
    
    for code in CODE_LIST:
        
        fp = csv.reader(open("./BigData/files/"+code+".csv","rb"))
    
        for f in fp:
           
            if f[0] == "31-December-2014":
                #print "in if"
                lastCp[code] = f[4] 
              
            elif f[0] == "1-January-2014":
                #print "in elif"
                firstCp[code] = f[4]
              
            else :
                continue
    
    
    for code in CODE_LIST:
        last = float(lastCp[code])
        first = float(firstCp[code])
                 
        gain = (last - first) / first
        perchange = round ((gain * 100),2)
        
        gainper[code] = perchange
        sorted_values = sorted(gainper.items(), key=operator.itemgetter(1), reverse=True)
    
    r = 99.00       
    for i in sorted_values:
        u,v = i
        print u,v
        yRank[u] = r/100.00
        r = r-1
    
    for key in yRank:
       print "code : ",key," rank: ",yRank[key]
      
def main():
    loadData()
    yearWise()
   
if __name__ == "__main__":
    main() 