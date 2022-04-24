class UndergroundSystem:

    def __init__(self):        
        self.idx = dict()
        self.eval = dict() 
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.idx[id] = [stationName, t]
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        start, time = self.idx[id]
        del self.idx[id]
        
        trip_time = t - time
        if (start, stationName) not in self.eval:
            self.eval[(start, stationName)] = [trip_time, 1]
        else:
            self.eval[(start, stationName)][0] += trip_time
            self.eval[(start, stationName)][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:                
        total, count = self.eval[(startStation, endStation)]
        return total / count                          

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)