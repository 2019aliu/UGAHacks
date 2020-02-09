import stock

class User:
	def __init__(self, stockList)
		self.liquidAssets = 10000
		self.stocksBought = {stock: 0 for stock in stockList}
		self.stockShorted = {stock: 0 for stock in stockList}
		self.totalAssets = 0
		self.done = false
		self.success = false

	def getStockList():
		return stocksBought

	def buyStock(stock):
		if (liquidAssets >= stock.getPrice()):
			stocksBought[stock.ticker] = stocksBought[stock.ticker] + 1
			liquidAssets = liquidAssets - stock.getPrice()

	def buyShort(stock):
		if (liquidAssets >= stock.getPrice()):
			stocksShorted[stock.ticker] = stocksShorted[stock.ticker] + 1

	def sellStock(stock):
		if (stocksBought[stock.ticker] >= 1):
			stocksBought[stock.ticker] = stocksBought[stock.ticker] - 1
			liquidAssets = liquidAssets + stock.getPrice()

	def sellShort(stock):
		if (stockShorted[stock.ticker] >= 1):
			stocksShorted[stock.ticker] = stocksShorted[stock.ticker] - 1

	def getTotalAssets():
		listTick = ['BLK', 'AAPL', 'NYT', 'DIS', 'GE', 'JPM', 'MSFT']
    	count = 0
    	totalAssets = liquidAssets
    	while (count < len(listTick)):
			totalAssets = totalAssets + stocksBought[listTick[count]]
			count++
		return totalAssets

	def checkSuccessAndTime(stock1):
		count = 0
		getTotalAssets()
		if (totalAssets > stock1.getThreshold()):
			success = true
			done = true
		totalAssets = 0


user = new User()
print(user.liquidAssets)