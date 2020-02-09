class Level:
    def __init__(self, startDate, threshold):
        self.numDays = 0
        self.startDate = startDate
        self.threshold = threshold

    def getNumDays(self):
        return self.numDays
    
    def setNumDays(self, newNaps):
    	self.numDays = newNaps

    def getThreshold():
    	return self.threshold