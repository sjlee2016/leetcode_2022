class UndergroundSystem(object):

    def __init__(self):
        self.checkInHistory = {}
        self.travelLogs = {} 
    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.checkInHistory[id] = (stationName,t)
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        (startStation, startTime ) = self.checkInHistory[id]
        if (startStation,stationName) not in self.travelLogs :
            self.travelLogs[(startStation,stationName)] = [t-startTime,1]
        else :
            self.travelLogs[(startStation,stationName)][0] += (t-startTime)
            self.travelLogs[(startStation,stationName)][1] += 1
    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """
        return (1.0 * self.travelLogs[(startStation,endStation)][0]) / self.travelLogs[(startStation,endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)