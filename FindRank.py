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
    
    print CODE_LIST
    for code in CODE_LIST:
        
        fp = csv.reader(open("./BigData/files/"+code+".csv","rb"))
        
        for f in fp:
           # d = f[0].split("-")
            lastCp = 0
            firstCp = 0
            
            if f[0] == "31-December-2014":
                #print "in if"
                lastCp = f[4] 
                print code,"L:",lastCp
                
            elif f[0] == "01-January-2014":
                print "in elif"
                firstCp = f[4]
                print "F:",firstCp
                
            else :
                continue
            
            #perchange = (lastCp - firstCp)/firstCp
            #print code,":",perchange
            #print code, round(perchange,2)
        

def main():
    loadData()
    yearWise()
   
if __name__ == "__main__":
    main() 