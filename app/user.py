from stock import Stock
from level import Level
from datetime import *

class User:
	def __init__(self, stockList, level):
		self.liquidAssets = 100000
		self.stocksBought = {stock: 0 for stock in stockList}
		self.stocksShorted = {stock: 0 for stock in stockList}
		self.stockObjects = [Stock(stock) for stock in stockList]
		self.updatedStockValues = {stock: stonk.getPrice() for stock, stonk in zip(stockList, self.stockObjects)}
		self.totalAssets = 0
		self.done = False
		self.success = False
		self.short = 0
		self.previousDate = 0
		self.currentDate = 0
		self.level = level
		self.stockList = stockList

	def getLevel(self):
		return self.level

	def getHistoricalData(self):
		historicD = {stock: {} for stock in self.stockList}
		count = 0
		while (count < len(historicD)):
			self.stockObjects[count].setDate(datetime(2003, 1, 2))
			historicD[self.stockObjects[count].getTicker()] = self.stockObjects[count].updatePriceWithNumDays(7)
			count += 1
		return historicD


	def getStockList(self):
		return self.stocksBought

	def buyStock(self, stock):
		if (self.liquidAssets >= stock.getPrice()):
			self.stocksBought[stock.ticker] += 1
			self.liquidAssets = self.liquidAssets - stock.getPrice()
			self.short += 1

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
			self.short -= 1



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
				if self.short > 0:
					self.totalAssets -= self.stocksShorted[listTick[count]] * 0.05 * self.updatedStockValues[listTick[count]] * (currentDate-previousDate)
			except:
				print("")
			count += 1
		self.previousDate = self.currentDate
		return self.totalAssets

	def checkSuccessAndTime(self, level):
		count = 0
		getTotalAssets()
		if (self.totalAssets > level.getThreshold()):
			self.success = True
			self.done = True
		self.totalAssets = 0

user = User({'BLK', 'AAPL', 'JPM', 'MSFT'}, Level(105000))
print(user.getHistoricalData())