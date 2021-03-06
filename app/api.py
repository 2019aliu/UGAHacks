from user import User
from level import Level
from stock import Stock
from datetime import *

import db

# input: ticker --> quantity (pos or neg)
def makeTransactions(buys, shorts):
    for buy in buys:
        # buy
        if (buys[buy] > 0):
            for i in range(buys[buy]):
                myUser.buyStock(buy)
        # sell
        else:
            for i in range(0 - buys[buy]):
                myUser.sellStock(buy)
    for short in shorts:
        # buy
        if (shorts[short] > 0):
            for i in range(shorts[short]):
                myUser.buyShort(short)
        # sell
        else:
            for i in range(0 - shorts[short]):
                myUser.sellShort(short)

    # maybe provide a final valuation here?

def initializeLevelOne():
    level1 = Level(105000, "2003-02-01")
    myUser = User(['AAPL', 'BLK', 'MSFT', 'JPM'], level1)
    return myUser

def initializeLevelTwo():
    level2 = Level(107000, "2016-01-01")
    myUser = User(['AAPL', 'BLK', 'MSFT', 'JPM'], level2)
    return myUser

def initializeLevelThree():
    level3 = Level(110000, "2008-01-01")
    myUser = User(['BLK', 'AAPL', 'NYT', 'DIS', 'GE', 'JPM', 'MSFT'], level3)
    return myUser

def getNewValuation(inputUser):
    return inputUser.getTotalAssets()

def getStocksBought():
    return myUser.getStockList()

def getShortsBought():
    return myUser.getShortList()

def getStockCost(ticker):
    name = db.stockTickers.find_one({"Ticker": ticker})['Name']
    stockData = db.stocksOhTwo.find_one({"stringDate": "2002-01-04"})
    return stockData[name]
