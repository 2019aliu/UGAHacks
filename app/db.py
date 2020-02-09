from flask import Flask
from flask_pymongo import pymongo

CONNECTION_STRING = "mongodb+srv://admin:admin@cluster0-hsmxr.gcp.mongodb.net/test?retryWrites=true&w=majority"
# for Python3.4 or later: mongodb://admin:<password>@cluster0-shard-00-00-hsmxr.gcp.mongodb.net:27017,cluster0-shard-00-01-hsmxr.gcp.mongodb.net:27017,cluster0-shard-00-02-hsmxr.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority
#

client = pymongo.MongoClient(CONNECTION_STRING)

# Stock data from the companies we chose
stockData = client.get_database('stockData')
stocksOhTwo = stockData.get_collection('sevenStocksFrom2002')
stockTickers = stockData.get_collection('stockTickers')

# print(stocksOhTwo.find_one({"Date": 1009930000000})['Date'])

# this method takes in mappings from ticker to the company name
# this method will add the ticker-name pairings to the collection for tickers
def addTickersToDB(tickerMap):  # lol tickerDict sounds weird
    for ticker in tickerMap:
        stockTickers.insert_one({"Ticker": ticker, "Name": tickerMap[ticker]})

print(stockTickers.find_one({'Name': 'Apple'})['Name'])


# addTickersToDB({"AAPL": "Apple", "BLK": "BlackRock", "DIS": "Disney", "GE": "GE", "JPM": "JPMorgan", "MSFT": "Microsoft", "NYT": "New York Times"})
