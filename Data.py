import urllib
import csv

data = csv.reader(open("./data/BSE100.csv","rb"))
tickets = []

for row in data:
    tickets.append(row[0])
    

for tic in tickets:
    url = "http://real-chart.finance.yahoo.com/table.csv?s="+tic+"&a=00&b=21&c=2014&d=00&e=21&f=2015&g=d&ignore=.csv"
   
     
    opener = urllib.FancyURLopener({})
    f = opener.open(url)
     
    html = f.read()
    fo = open("./data/files/"+tic+".csv", "w")
    fo.write(html)
    fo.close()
    #print url
    
print "download complete"

