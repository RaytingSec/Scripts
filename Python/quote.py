#!/usr/bin/python3
# Streaming stock quotes using yahoo api

import time
from requests import get
import sys

ticker = ""
if len(sys.argv) > 1:
    ticker = sys.argv[1]
else:
    sys.exit("No ticker!")

url = "http://download.finance.yahoo.com/d/quotes.csv?s={}&f=l1c1".format(ticker)


def getQuote(ticker):
    # '24.86,+5.46'
    req = get(url.format(ticker)).text.strip('\n')
    req = req.split(',')
    price = float(req[0])
    change = float(req[1])
    perc = change / price
    # perc = round(change / price, 4)
    return (price, change, perc)


def prettyPrint(quote):
    price = str(quote[0])

    change = quote[1]
    if change > 0:
        change = '+' + str(change)
    else:
        change = str(change)

    perc = str(round(quote[2] * 100, 2))
    perc += '%'

    result = "({}, {}, {})".format(price, change, perc)

    return result


while True:
    try:
        quote = getQuote(ticker)
        # print(quote)
        print(prettyPrint(quote))
        time.sleep(5)
    except KeyboardInterrupt:
        print("\nExiting")
        sys.exit()
