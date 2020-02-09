from stock import Stock
from level import Level
from datetime import *

class User:
	'''
	stockList: the list of stocks permitted in the level
	level: the level that user is currently working on. This is just a level object
	LiquidAssets: amount of currently available assets
	stocksBought: stock ticker --> number of shares bought
	stocksShorted: stock ticker --> number of shares shorted
	stockValues: stock ticker --> current price
	totalAssets: total value of User, calculated by amount of liquid assets added to stocksBought and stocksShorted
	done: whether the user has finished
	
	'''
	def __init__(self, stockList, level):
		self.stockList = stockList
		self.level = level
		self.liquidAssets = 100000
		self.stocksBought = {stock: 0 for stock in stockList}
		self.stocksShorted = {stock: 0 for stock in stockList}
		self.stockValues = {ticker: Stock(ticker).getPrice() for ticker in stockList}
		self.totalAssets = 0
		self.ipo = {'AAPL': 22, 'BLK': 14, 'DIS': 13.88, 'GE': 0.8, 'JPM': 9.78, 'MSFT': 21, 'NYT': 42}
	'''
	Getters
	'''

	# get the level, which holds the startingDate
	def getLevel(self):
		return self.level

	def getCurrentDate(self):
		return self.level.getCurrentDate()

	def getHistoricalData(self):
		historicD = {stock: [] for stock in self.stocksBought}
		# historicD = {stock: [] for stock in self.stocksBought}
		for stockTicker in historicD:
			ipoPrice = self.ipo[stockTicker]
			tempStock = Stock(stockTicker)
			for i in range(7):
				dateString = str(self.level.getCurrentDate() - timedelta(days=i))[:10]
				historicD[stockTicker].append((dateString, tempStock.getPastData()[i] * ipoPrice))
		return historicD

	def getStockList(self):
		return self.stockList

	def getStocksBought(self):
		return self.stocksBought
	
	def getTotalAssets(self):
		self.calculateTotalAssets()
		return self.totalAssets
	
	# REMOVE THIS, IT IS JUST FOR TESTING
	def getStockValues(self):
		return self.stockValues

	'''
	Buying and selling stocks and shorts
	'''

	def buyStock(self, stockTicker, quantity):
		for i in range(quantity):
			self.buyStock(stockTicker)

	def buyStock(self, stockTicker):
		stockOBJ = Stock(stockTicker)
		if (self.liquidAssets < stockOBJ.getPrice()):
			raise ValueError('You do not have enough liquid assets to purchase this stock.')
		else:
			self.stocksBought[stockTicker] += 1
			self.liquidAssets -= stockOBJ.getPrice()
	
	def sellStock(self, stockTicker):
		stockOBJ = Stock(stockTicker)
		if (self.stocksBought[stockTicker] == 0):
			raise ValueError('You do not have stocks of this ticker to sell.')
		else:
			self.stocksBought[stockTicker] -= 1
			self.liquidAssets += stockOBJ.getPrice()

	# TODO: fix buying and selling shorts
	def buyShort(self, stock):
		self.stocksShorted[stock.ticker] += 1
		self.liquidAssets = self.liquidAssets + self.stockShorted[stock.ticker].getPrice()
		if (self.previousDate == 0):
			self.previousDate = self.level.getNumDays()
		self.currentDate = self.level.getNumDays()

	def sellShort(self, stock):
		if (self.stockShorted[stock.ticker] >= 1 and self.liquidAssets >= stock.getPrice()):
			self.stocksShorted[stock.ticker] -= 1
			self.liquidAssets = self.liquidAssets - self.stockShorted[stock.ticker].getPrice()

	# so this method can be done a lot more pythonically
	# BUT I'm desperate so no (and also easier debugging -- wait I don't debug oopsies)
	def calculateTotalAssets(self):
		interest = 0.05
		newValuation = self.liquidAssets
		# bStock is a stock ticker
		for bStock in self.stocksBought:
			newValuation += self.stocksBought[bStock] * self.stockValues[bStock]
		for sStock in self.stocksShorted:
			newValuation -= self.stocksShorted[sStock] * self.stockValues[sStock] * (1 + interest)
		self.totalAssets = newValuation

	def updateTime(self, numDays):
		self.level.addNumDays(numDays)
		# update the stock prices
		for ticker in self.stockValues:
			# self.stockValues[ticker] = Stock(ticker, self.level.getCurrentDate()).getPrice()
			s = Stock(ticker)
			s.updatePriceWithDate(self.level.getCurrentDate())
			self.stockValues[ticker] = s.getPrice()
		self.calculateTotalAssets()

	def checkSuccess(self):
		self.calculateTotalAssets()
		return totalAssets > level.getThreshold()
	
	def checkFailure(self):
		self.calculateTotalAssets()
		return self.level.getNumDays() >= 365 and totalAssets < 0
