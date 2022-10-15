class UndergroundSystem:

    def __init__(self):
        self.check_in = {}
        self.time_taken = {} 
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.check_in[id]
        if (startStation, stationName) not in self.time_taken :
            self.time_taken[(startStation,stationName)] = [t-startTime, 1]
        else :
            self.time_taken[(startStation,stationName)][0] += t-startTime
            self.time_taken[(startStation,stationName)][1] += 1
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.time_taken[(startStation,endStation)][0] / self.time_taken[(startStation,endStation)][1] 


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)