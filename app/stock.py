import db
from datetime import *

class Stock:
	# args are all arguments that are single value (i.e. 7, true)
	# kwargs are all arguments that are key-value pair (i.e. name="John", hardMode=true)
	def __init__(self, ticker, name, price=0, date=date(2003, 1, 24)):
		self.ticker = ticker
		self.name = name
		self.price = price
		self.date = date
		self.data = []
		for i in range(7):
			self.data.append(db.stocksOhTwo.find_one({"stringDate": str(self.date - timedelta(days=i))})[self.name])
	
	def __init__(self, ticker, date=date(2003, 1, 24)):
		self.ticker = ticker
		name = db.stockTickers.find_one({"Ticker": ticker})['Name']
		self.name = name
		stockData = db.stocksOhTwo.find_one({"stringDate": "2003-01-24"})
		self.price = stockData[name]
		self.date = date
		self.data = []
		for i in range(7):
			self.data.append(db.stocksOhTwo.find_one({"stringDate": str(self.date - timedelta(days=i))})[self.name])
	
	def getPrice(self):
		return self.price
	
	def getPastData(self):
		return self.data

	def getTicker(self):
		return self.ticker

	def setDate(self, date):
		self.date = date

	def updatePriceWithDate(self, day):
		# newDate = datetime.strptime(day, "%Y-%m-%d")
		# self.price = db.stocksOhTwo.find_one({"stringDate": newDate})[self.name]
		self.price = db.stocksOhTwo.find_one({"stringDate": str(day)})[self.name]
		self.date = day
		self.data = []
		for i in range(7):
			self.data.append(db.stocksOhTwo.find_one({"stringDate": str(self.date - timedelta(days=i))})[self.name])
		# return self.price
	
	def updatePriceWithNumDays(self, numDays):
		self.price = db.stocksOhTwo.find_one({"stringDate": str(self.date + timedelta(days=numDays))})
		self.date = self.date + timedelta(days=numDays)
		self.data = []
		for i in range(7):
			insideList = []
			insideList.append(db.stocksOhTwo.find_one({"stringDate": str(self.date - timedelta(days=i))}))
			insideList.append(str(self.date - timedelta(days=i)))
			insideList.append("hi")
			self.data.append(insideList)

# testS = Stock("AAPL")
# print(testS.getPrice())