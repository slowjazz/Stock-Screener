import csv
import urllib

stock=raw_input("Please enter at least one ticker symbol: ")

stock.replace(" ","")

ref="http://finance.yahoo.com/d/quotes.csv?s="+str(stock)+"&f=npr"

str(ref)

urllib.urlretrieve(ref,"quotes.csv")

data = csv.reader(open('quotes.csv', 'rb'))

n=[]
p=[]
e=[]

for row in data:
    n.append(row[0])
    p.append(eval(row[1]))
    e.append(eval(row[2]))

print str(len(n))+" companies' shares data retrieved."

data2={}

data2["Names"]=n
data2["Prices"]=p
data2["e Value"]=e

print data2

##DATA INTERPRETATION USING DICTIONARY data2



raw_input("Press any key to exit")
