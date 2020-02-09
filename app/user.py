import stock

class User:
	def __init__(self)
		self.liquidAssets = 10000
		self.stocksBought = {'BLK': 0, 'AAPL': 0, 'NYT': 0, 'DIS': 0, 'GE': 0, 'JPM': 0, 'MSFT': 0}
		self.stocksShorted = {'BLK': 0, 'AAPL': 0, 'NYT': 0, 'DIS': 0, 'GE': 0, 'JPM': 0, 'MSFT': 0}
		self.totalAssets = 0
		self.done = false
		self.success = false

	def buyStock(stock.ticker):
		if (liquidAssets >= stock.getPrice()):
			stocksBought[stock.ticker] = stocksBought[stock.ticker] + 1
			liquidAssets = liquidAssets - stock.getPrice()

	def buyShort(stock.ticker):
		if (liquidAssets >= stock.getPrice()):
			stocksShorted[stock.ticker] = stocksShorted[stock.ticker] + 1
		
	def sellStock(stock.ticker):
		if (stocksBought[stock.ticker] >= 1):
			stocksBought[stock.ticker] = stocksBought[stock.ticker] - 1
			liquidAssets = liquidAssets + stock.getPrice()

	def sellShort(stock.ticker):
		if (stockShorted[stock.ticker] >= 1):
			stocksShorted[stock.ticker] = stocksShorted[stock.ticker] - 1

	def checkSuccessAndTime(threshold):
		count = 0
		totalAssets = liquidAssets + stocksBought['BLK'] + stocksBought['AAPL'] + stocksBought['NYT'] + stocksBought['DIS'] + stocksBought['GE'] + stocksBought['JPM'] + stocksBought['MSFT']
		if (totalAssets > threshold):
			success = true
			done = true


user = new User()
print(user.liquidAssets)