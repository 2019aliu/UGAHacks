class Level:
    def __init__(self, startDate, threshold):
        self.numDays = 0
        self.startDate = startDate
        self.threshold = threshold

    def getNumDays(self):
        return self.numDays
    
    def addNumDays(self, numDays):
        if self.numDays + numDays > 365:
            raise ValueError('The time limit of 365 days has been exceeded when fast forwarding by %d days' % numDays)
        self.numDays += numDays

    def getThreshold(self):
    	return self.threshold