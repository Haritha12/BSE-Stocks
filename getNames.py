from bs4 import BeautifulSoup
import csv
import urllib
import codecs



#print tabulka.text.encode
#print tabulka
#b = open('C:/Users/Praveen Reddy/Desktop/DADV/revenues.csv', 'w')
#a = csv.writer(b)

data = csv.reader(open("./data/BSE100.csv","rb"))

names = {}
name = []
for row in data:
    name.append(row[0])
    #names[row[0]] = row[1]
list = []
for n in name:
    url = "https://in.finance.yahoo.com/q/hp?a=00&b=21&c=2014&d=00&e=22&f=2015&g=d&s="+n+"&ql=1"
    print "============"+n+"================"
    reven = []
    reven.append(n)
    response = urllib.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    n1 = []
    n1.append(n)
    d = soup.find("div", {'class' : 'title'})
    if d is not None:
        for row in d.findAll("h2"):
            print row.text
            n1.append(row.text)
    else:
        print "none"
        n1.append("none")
    list.append(n1)
        
resultFyle = open("./data/bsenames.csv",'wb')

# Create Writer Object
wr = csv.writer(resultFyle, dialect='excel')
wr.writerows(list)
    
                    
                        
                    
                    
    
                
                
        

