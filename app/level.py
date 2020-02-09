class Level:
    def __init__(self, startDate, threshold):
        self.numDays = 0
        self.startDate = startDate
        self.threshold = threshold

    def getNumDays(self):
        return self.numDays
    
    def addNumDays(self, numDays):
        if self.numDays + numDays > self.threshold:
            raise ValueError('The time limit of %d has been exceeded when fast forwarding by %d days' % (self.threshold, numDays))
        self.numDays += numDays

    def getThreshold(self):
    	return self.threshold