from stock import Stock
from level import Level
from datetime import *

class User:
	'''
	stockList: the list of stocks permitted in the level
	LiquidAssets: amount of currently available assets
	stocksBought: stock ticker --> number of shares bought
	stocksShorted: stock ticker --> number of shares shorted
	stockObjects: list of Stock Objects
	updateStockValues: stock ticker --> current price
	totalAssets: total value of User, calculated by amount of liquid assets added to stocksBought and stocksShorted
	done: whether the user has finished
	
	'''
	def __init__(self, stockList, level):
		self.stockList = stockList
		self.level = level
		self.liquidAssets = 100000
		self.stocksBought = {stock: 0 for stock in stockList}
		self.stocksShorted = {stock: 0 for stock in stockList}
		self.stockObjects = [Stock(stockTicker) for stockTicker in stockList]
		self.updatedStockValues = {stock: stonk.getPrice() for stock, stonk in zip(stockList, self.stockObjects)}
		self.totalAssets = 0
		self.done = False

	# get the level, which holds the startingDate
	def getLevel(self):
		return self.level

	def getCurrentDate(self):
		return self.level.getCurrentDate()

	def getHistoricalData(self):
		historicD = {stock: {} for stock in self.stocksBought}
		# historicD = {stock: [] for stock in self.stocksBought}
		for stockTicker in historicD:
			tempStock = Stock(stockTicker)
			for i in range(7):
				dateString = str(self.level.getCurrentDate() - timedelta(days=i))[:10]
				historicD[stockTicker][dateString] = tempStock.getPastData()[i]
			# historicD[stockTicker] = tempStock.getPastData()
		return historicD

	def getStockList(self):
		return self.stockList

	def getStocksBought(self):
		return self.stocksBought

	def buyStock(self, stockTicker):
		stockOBJ = Stock(stockTicker)
		buyStock(self, stockOBJ)

	def buyStock(self, stock):
		if (self.liquidAssets >= stock.getPrice()):
			self.stocksBought[stock.ticker] += 1
			self.liquidAssets = self.liquidAssets - stock.getPrice()
			# self.short += 1

	def buyShort(self, stock):
		self.stocksShorted[stock.ticker] += 1
		self.liquidAssets = self.liquidAssets + self.stockShorted[stock.ticker].getPrice()
		if (self.previousDate == 0):
			self.previousDate = self.level.getNumDays()
		self.currentDate = self.level.getNumDays()


	def sellStock(self, stock):
		if (self.stocksBought[stock.ticker] >= 1):
			self.stocksBought[stock.ticker] -= 1
			self.liquidAssets = self.liquidAssets + stock.getPrice()

	def sellShort(self, stock):
		if (self.stockShorted[stock.ticker] >= 1 and self.liquidAssets >= stock.getPrice()):
			self.stocksShorted[stock.ticker] -= 1
			self.liquidAssets = self.liquidAssets - self.stockShorted[stock.ticker].getPrice()
			# self.short -= 1



	def getTotalAssets(self):
		listTick = ['BLK', 'AAPL', 'NYT', 'DIS', 'GE', 'JPM', 'MSFT']
		count = 0
		self.totalAssets = self.liquidAssets
		while (count < len(listTick)):
			try:
				self.totalAssets = self.totalAssets + self.stocksBought[listTick[count]]
			except:
				print("")

			try:
				if len(self.stocksShorted) > 0:
					self.totalAssets -= self.stocksShorted[listTick[count]] * 0.05 * self.updatedStockValues[listTick[count]]
					# self.totalAssets -= self.stocksShorted[listTick[count]] * 0.05 * self.updatedStockValues[listTick[count]] * (currentDate-previousDate)
			except:
				print("")
			count += 1
		# self.previousDate = self.currentDate
		return self.totalAssets

	def checkSuccessAndTime(self, level):
		count = 0
		getTotalAssets()
		if (self.totalAssets > level.getThreshold()):
			self.done = True
		self.totalAssets = 0
