#This is a Python parser that parses stock data from Yahoo Finance to save it in *.csv format

import csv
import urllib.request

url = 'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_date}&period2={end_date}&interval=1d&events=history'

# Replace {ticker} with the desired stock ticker symbol
# Replace {start_date} and {end_date} with the desired start and end dates in Unix timestamp format
url = url.format(ticker='TSLA', start_date=0, end_date=9999999999)

response = urllib.request.urlopen(url)
data = response.read()

reader = csv.reader(data.decode('utf-8').splitlines())

# Print the header row
header = next(reader)
print(header)

# Print each row of data
for row in reader:
    print(row)
