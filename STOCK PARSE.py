import csv
import urllib

stock=raw_input("Please enter at least one stock ticker symbol : ")

ref="http://finance.yahoo.com/d/quotes.csv?s="+str(stock)+"&f=pr"

print ref

# RETRIEVE CSV FILE
#with open('quote.csv', 'rb') as csvfile:
#   data = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in data:
#         print ', '.join(row)

data = csv.reader(open('quote.csv', 'rb'))
for row in data:
    price = row[0]
    e = row[1]
print price
print e
