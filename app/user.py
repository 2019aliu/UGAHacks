class User:
	def __init__(self)
		self.liquidAssets = 10000
		self.stocksBought = {'BLK': 0, 'AAPL': 0, 'NYT': 0, 'DIS': 0, 'GE': 0, 'JPM': 0, 'MSFT': 0}
		self.stocksShorted = {'BLK': 0, 'AAPL': 0, 'NYT': 0, 'DIS': 0, 'GE': 0, 'JPM': 0, 'MSFT': 0}
		self.totalAssets = 10000

	def buyStock(stock):
		if (liquidAssets >= stock.getPrice()):
			stocksBought[stock] = stocksBought[stock] + 1
			liquidAssets = liquidAssets - stock.getPrice()

	def buyShort(stock):
		if (liquidAssets >= stock.getPrice()):
			stocksShorted[stock] = stocksShorted[stock] + 1
		
	def sellStock(stock):
		if (stocksBought[stock] >= 1):
			stocksBought[stock] = stocksBought[stock] - 1
			liquidAssets = liquidAssets + stock.getPrice()

	def sellShort(stock):
		if (stockShorted[stock] >= 1):
			stocksShorted[stock] = stocksShorted[stock] - 1

	# def update(time):

	def checkSuccessAndTime(threshold):
		while ():
			totalAssets = liquidAssets + stocksBought[]


user = new User()
print(user.liquidAssets)