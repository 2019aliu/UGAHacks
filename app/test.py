from level import Level
from stock import Stock
import datetime

# testL = Level("8/6/09", 365)
# testL.addNumDays(300)
# testL.addNumDays(105)
# print(testL.getNumDays())


testStock = Stock("AAPL")
print(testStock.getPrice())
testStock.updatePriceWithDate(datetime.date(2004, 5, 17))
print(testStock.getPrice())