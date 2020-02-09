import stock
import level

class User:
	def __init__(self, getStockList)
		self.liquidAssets = 10000
		self.stocksBought = {stock: 0 for stock in stockList}
		self.stockShorted = {stock: 0 for stock in stockList}
		self.updatedStockValues = {(stock): Stock(updatedStockValues[(stock)]).getPrice() for stock in stockList}
		self.totalAssets = 0
		self.done = false
		self.success = false
		self.short = 0;

	def getStockList(self):
		return stocksBought

	def buyStock(self, stock):
		if (self.liquidAssets >= stock.getPrice()):
			self.stocksBought[stock.ticker] += 1
			self.liquidAssets = self.liquidAssets - stock.getPrice()
			self.short++

	def buyShort(self, stock):
		self.stocksShorted[stock.ticker] += 1
		self.liquidAssets = self.liquidAssets + self.stockShorted[stock.ticker].getPrice()

	def sellStock(self, stock):
		if (self.stocksBought[stock.ticker] >= 1):
			self.stocksBought[stock.ticker] -= 1
			self.liquidAssets = self.liquidAssets + stock.getPrice()

	def sellShort(self, stock):
		if (self.stockShorted[stock.ticker] >= 1 and self.liquidAssets >= stock.getPrice()):
			self.stocksShorted[stock.ticker] -= 1
			self.liquidAssets = self.liquidAssets - self.stockShorted[stock.ticker].getPrice()
			self.short--

	def getTotalAssets(self):
		listTick = ['BLK', 'AAPL', 'NYT', 'DIS', 'GE', 'JPM', 'MSFT']
    	count = 0
    	self.totalAssets = self.liquidAssets
    	while (count < len(listTick)):
			self.totalAssets = self.totalAssets + self.stocksBought[listTick[count]]
			if self.short > 0:
				self.totalAssets -= self.stocksShorted[listTick[count]] * 0.05 * self.updatedStockValues[listTick[count]]
			count++
		return self.totalAssets

	def checkSuccessAndTime(self, level):
		count = 0
		getTotalAssets()
		if (self.totalAssets > level.getThreshold()):
			self.success = true
			self.done = true
		self.totalAssets = 0