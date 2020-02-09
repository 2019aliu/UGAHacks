import db
from datetime import date

class Stock:
	# args are all arguments that are single value (i.e. 7, true)
	# kwargs are all arguments that are key-value pair (i.e. name="John", hardMode=true)
	def __init__(self, ticker, name, price=0, date=date(2003, 1, 18)):
		self.ticker = ticker
		self.name = name
		self.price = price
		self.date = date
	
	def __init__(self, ticker):
		self.ticker = ticker
		name = db.stockTickers.find_one({"Ticker": ticker})['Name']
		self.name = name
		stockData = db.stocksOhTwo.find_one({"stringDate": "2003-01-18"})
		self.price = stockData[name]
		self.date = date(2003, 1, 18)
	
	def getPrice(self):
		return self.price

	def updatePrice(self, day):
		price = db.stocksOhTwo.find_one({"stringDate": day})[self.name]
		return price

# testS = Stock("AAPL")
# print(testS.getPrice())