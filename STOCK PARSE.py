from datetime import datetime 
import csv
import urllib
from collections import defaultdict

stock=raw_input("Please enter at least one ticker symbol: ")

stock.replace(" ","")
#Removes whitespace in input

ref="http://finance.yahoo.com/d/quotes.csv?s="+str(stock)+"&f=npr"
#concatenates url for data retrieval

str(ref)
#ensures ref is a string

urllib.urlretrieve(ref,"quotes.csv")
#retrieves csv over http

data = csv.reader(open('quotes.csv', 'rb'))
#opens and parses data using csv module

n=[]
p=[]
e=[]
for row in data:
    n.append(str(row[0]))
    p.append(eval(row[1]))
    e.append(eval(row[2]))
#puts data from each columns 1-3 into 3 lists

print str(len(n))+" companies' shares data retrieved."
#confirmation for user

data2=defaultdict(list)
#allows keys and value to be assigned at the same time

k=0
for key in n:
	data2[key].append(p[k])
	data2[key].append(e[k])
	k=k+1

#consolidation of data to dictionary data2

print dict(data2)
time=datetime.now()
print "Last updated" '%s/%s/%s' % (time.hour, time.minute, time.second) 
#DATA INTERPRETATION USING DICTIONARY data2

raw_input("Press any key to exit") #so the prorgram doesnt steal your fap
