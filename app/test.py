from level import Level
from stock import Stock
from user import User
from api import *
import datetime

# testL = Level("8/6/09", 365)
# testL.addNumDays(300)
# testL.addNumDays(105)
# print(testL.getNumDays())


# testStock = Stock("AAPL")
# print(testStock.getPrice())
# print("\n\n\n")
# testStock.updatePriceWithNumDays(369)
# print(testStock.getPrice())
# print("\n\n\n")
# print(testStock.getPastData())
# print("\n\n\n")

testUser = User(['AAPL', 'BLK'], Level(101, "2004-03-01"))
print(testUser.getHistoricalData())
# testUser.buyStock(Stock('AAPL'))
testUser.buyStock("AAPL")
print(testUser.getStocksBought())
print(testUser.getTotalAssets())
# print("\n\n\n")
# print(testUser.getStockValues())
testUser.updateTime(7)
print(testUser.getTotalAssets())
# print(testUser.getStockValues())


