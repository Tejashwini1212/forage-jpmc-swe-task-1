################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import sys
import urllib.request

# Given an array of stock data, find the ratio of the two prices
def getRatio(price_a, price_b):
    """ Get ratio of price_a to price_b. """
    if price_b == 0:
        return
    return price_a / price_b

# Fetch and format data from the API
def getDataPoint(quote):
    """ Produce all of the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

# Main function
if __name__ == "__main__":
    # Query the API once every N seconds and update stock data
    for _ in range(500):
        quotes = json.loads(urllib.request.urlopen("http://localhost:8080/query?datatype=json").read())

        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

        price_a = getDataPoint(quotes[0])[3]
        price_b = getDataPoint(quotes[1])[3]
        print(f"Ratio {getRatio(price_a, price_b)}")
