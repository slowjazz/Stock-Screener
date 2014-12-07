import csv
import urllib

stock=raw_input("Please enter at least one stock ticker symbol : ")

ref="http://finance.yahoo.com/d/quotes.csv?s="+str(stock)+"&f=pr"

str(ref)

urllib.urlretrieve(ref,"quotes.csv")

data = csv.reader(open('quotes.csv', 'rb'))
for row in data:
    price = row[0]
    e = row[1]
print price
print e
