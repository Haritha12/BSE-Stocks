import Tkinter as tk
import csv
import pprint
import urllib
import csv
import operator


root = tk.Tk()
var = tk.StringVar(root)
 

CODE_LIST = []
BSE_CODE_NAMES = {}  
comp={}

# Function to display the dialog box 
def display():
    root.geometry("%dx%d+%d+%d" % (330, 80, 200, 150))
    root.title("Select company")
    names = BSE_CODE_NAMES.values()
    choices = names
    var.set('select')
    option = tk.OptionMenu(root, var, *choices)
    option.pack(side='left', padx=10, pady=10)    
    button = tk.Button(root, text="OK", command=ok)
    button.pack(side='left', padx=10, pady=10)        
    root.mainloop()


# Function to take action after clicking OK
def ok():
    company = var.get()
    print "-------------------------------------------"
    print "COMPANY NAME:",company 
    FindTopDaily(company)
    findTopMonthly(company)
    
    
#Funtion to load data about 100 companies
def loaddata():
    names = csv.reader(open("./NewData/BSE100.csv","rb"))
    for na in names:
        BSE_CODE_NAMES[na[0]] = na[1]
        CODE_LIST.append(na[0])
  

#Function to find the details of the number of days in which the company is topped in an year
def FindTopDaily(company):
    
    i=0
    for code in CODE_LIST:
            comp[i]=code
            i=i+1
    dict={}
    for x in CODE_LIST:
        dict[x]=0
    for i in range(0,224):
        fo = open("./NewData/temp_daily.csv", "rb")
        fo1= csv.reader(fo)
        #next(fo1, None)
        temp=[]
        for row1 in fo1:
            temp.append(row1[i]);
        dict[comp[temp.index(max(temp))]]=dict[comp[temp.index(max(temp))]]+int(1)
    i=0
    scores={}
    for x in CODE_LIST:
        scores[BSE_CODE_NAMES[x]]=dict[x]
        i=dict[x]+i
    sorted_scores_daily = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)

    print "TOP IN:      ",scores[company], "/225 days"
      
      
#Function to find the details of the number of months in which the company is at top in an year
def findTopMonthly(company):
    i=0
    for code in CODE_LIST:
            comp[i]=code
            i=i+1
            
    dict={}
    for x in CODE_LIST:
        dict[x]=0

    for i in range(0,12):
        fo = open("./NewData/temp_monthly.csv", "rb")
        fo1= csv.reader(fo)
        #next(fo1, None)
        temp=[]
        for row1 in fo1:
            #print i
            #print row1
            temp.append(row1[i]);
        dict[comp[temp.index(max(temp))]]=dict[comp[temp.index(max(temp))]]+int(1)
    i=0
    scores={}
    for x in CODE_LIST:
        scores[BSE_CODE_NAMES[x]]=dict[x]
        i=dict[x]+i

    sorted_scores_daily = sorted(scores.items(), key=operator.itemgetter(1),reverse=True)
    print "TOP IN:      ",scores[company], "/12 months"
    print "--------------------------------------"
      
        
         
def main():
    
    loaddata()
    display()

    


if __name__ == "__main__":
    main() 