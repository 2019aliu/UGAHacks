import db

class Stock:
	# args are all arguments that are single value (i.e. 7, true)
	# kwargs are all arguments that are key-value pair (i.e. name="John", hardMode=true)
	def __init__(self, ticker, name, price=0):
		self.ticker = ticker
		self.name = name
		self.price = price
	
	def __init__(self, ticker):
		self.ticker = ticker
		name = db.stockTickers.find_one({"Ticker": ticker})['Name']
		self.name = name
		stockData = db.stocksOhTwo.find_one({"stringDate": "2002-01-04"})
		self.price = stockData[name]
	
	def getPrice(self):
		return self.price

	def updatePrice(self, day):
		price = db.stocksOhTwo.find_one({"Date": day})[self.name]
		return price

testS = Stock("AAPL")
print(testS.getPrice())