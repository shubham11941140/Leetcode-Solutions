class UndergroundSystem:

    def __init__(self):
        
        self.idx = dict()
        self.eval = dict()
        
        self.cin = []
        self.cout = []        
        

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
        
        self.cout.append([id, stationName, t])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        
        
        total, count = self.eval[(startStation, endStation)]
        return total / count
        
        end = [[i[0], i[2]] for i in self.cout if i[1] == endStation]
        start = [[i[0], i[2]] for i in self.cin if i[1] == startStation]
        
        d = dict()
        for id, t in start:
            d[id] = [t]
        for id, t in end:
            if id in d:
                d[id].append(t)
        #print(d)
        for i in d:
            if len(d[i]) > 2:
                print(i)
        res = 0
        tot = 0
        for i in d:
            if len(d[i]) == 2:
                    if d[i][1] > d[i][0]:
                        res += (d[i][1] - d[i][0])
                        tot += 1
        return res / tot
            

        
        # Sort them by t
        #print("S", start[:10])
        #print("E", end[:10])
        start.sort(key=lambda x:x[0])
        end.sort(key=lambda x:x[0])
        #print("SS", start[:10])
        #print("SE", end[:10])
        ans = 0
        c = 0
        for i in start:
            for j in end:
                if i[0] == j[0] and i[1] < j[1]: 
                    ans += (j[1] - i[1])
                    c += 1
                    break
        return ans / c
                    
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)