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


def getQuote(q):
    # '24.86,+5.46'
    q = q.split(',')
    price = float(q[0])
    change = float(q[1])
    perc = (change / price).__round__(2)
    return (price, change, perc)


def prettyPrint(quote):
    price = str(quote[0])
    change = quote[1]
    perc = str((quote[2] * 100.0).__round__(4))

    if change > 0:
        change = '+' + str(change)
    # elif change < 0:
    #     change = '-' + str(change)
    else:
        change = str(change)
    perc += '%'

    result = "({}, {}, {})".format(price, change, perc)

    return result


while True:
    try:
        req = get(url).text.strip('\n')
        quote = getQuote(req)
        # print(quote)
        print(prettyPrint(quote))
        time.sleep(2)
    except KeyboardInterrupt:
        print("\nExiting")
        sys.exit()
