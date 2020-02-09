from datetime import *

class Level:
    def __init__(self, threshold, startingDate):
        self.numDays = 0
        self.threshold = threshold
        self.startingDate = datetime.strptime(startingDate, "%Y-%m-%d")

    def getStartingDate(self):
        return self.startingDate

    def getNumDays(self):
        return self.numDays

    def getCurrentDate(self):
        return self.startingDate + timedelta(days=self.numDays)

    def addNumDays(self, numDays):
        if self.numDays + numDays > 365:
            raise ValueError('The time limit of 365 days has been exceeded when fast forwarding by %d days' % numDays)
        self.numDays += numDays

    def getThreshold(self):
    	return self.threshold
