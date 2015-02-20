import Tkinter as tk
import csv
import pprint
import urllib
import csv
import operator
 

CODE_LIST = []
BSE_CODE_NAMES = {}  
comp={}

def loaddata():
    names = csv.reader(open("./NewData/BSE100.csv","rb"))
    for na in names:
        BSE_CODE_NAMES[na[0]] = na[1]
        CODE_LIST.append(na[0])
    
             
def LoadDailyDetailsIntoFile():
    fo = open("./NewData/temp_daily.csv", "wb")
    BSE_CODE_NAMES={}
    differences=[]
    
    i=0
    for code in CODE_LIST:
            comp[i]=code
            i=i+1
            prevb=float(0.0)
            y=float(0.0)
            name="./NewData/files/"+code+".csv"
            file = csv.reader(open(name,"rb"))
            temp={}
            temp["11"]=code
            next(file, None)
            for row1 in file:
                if y==0:
                    y=y+1
                    pass
                if y==1:
                    prevb=float(row1[4])
                    y=y+1
                else:                   
                    curr=float(row1[4])
                    x=float(float(curr)-float(prevb))
                    x=float(float(x)/float(curr))
                    prevb=row1[4]
                    temp[row1[0]]=(x)
            w = csv.DictWriter(fo,temp.keys())
            w.writerow(temp)
    
    

           
       
   
   
#To get ordered list of companies month wise     
# def FindTopMonthly(CODE_LIST,comp,company):
def LoadMonthlyDetailsIntoFile():
    fo = open("./NewData/temp_monthly.csv", "wb")
    BSE_CODE_NAMES={}
    differences=[]
    comp={}
    i=1
    for code in CODE_LIST:
        comp[i]=code
        i=i+1
        name="./NewData/files/"+code+".csv"
        file = csv.reader(open(name,"rb"))
        k=1
        monthly_closure={}
        for rec in file:
            if(k==21):
                dec_end=float(rec[4])
            if(k==42):
                monthly_closure["DECEMBER"]=(float(rec[4])-dec_end)/float(rec[4])
            if(k==43):
                nov_end=float(rec[4])
            if(k==60):
                monthly_closure["NOVEMBER"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==61):
                nov_end=float(rec[4])
            if(k==78):
                monthly_closure["OCTOBER"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==79):
                nov_end=float(rec[4])
            if(k==100):
                monthly_closure["SEPTEMBER"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==101):
                nov_end=float(rec[4])
            if(k==119):
                monthly_closure["AUGUST"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==120):
                nov_end=float(rec[4])
            if(k==141):
                monthly_closure["JULY"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==142):
                nov_end=float(rec[4])
            if(k==162):
                monthly_closure["JUNE"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==163):
                nov_end=float(rec[4])
            if(k==183):
                monthly_closure["MAY"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==184):
                nov_end=float(rec[4])
            if(k==201):
                monthly_closure["APRIL"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==202):
                nov_end=float(rec[4])
            if(k==222):
                monthly_closure["MARCH"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==223):
                nov_end=float(rec[4])
            if(k==241):
                monthly_closure["FEBRUARY"]=(float(rec[4])-nov_end)/float(rec[4])
            if(k==242):
                nov_end=float(rec[4])
            if(k==245):
                monthly_closure["JANUARY"]=(float(rec[4])-nov_end)/float(rec[4])
            k=k+1
         
        w = csv.DictWriter(fo,monthly_closure.keys())
        w.writerow(monthly_closure)
    

   
 
         
def main():
    loaddata()
    print "here"
    LoadDailyDetailsIntoFile()
    LoadMonthlyDetailsIntoFile()
    
    
#     FindTopMonthly("TATA CONSULTANCY SERVICES LTD.")
#     display()
    


if __name__ == "__main__":
    main() 