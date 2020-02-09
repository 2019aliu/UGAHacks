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
# testStock.updatePriceWithNumDays(369)
# print(testStock.getPrice())
# print(testStock.getPastData())


testUser = User(['AAPL', 'BLK'], Level(101, "2003-03-01"))
print(testUser.getHistoricalData())