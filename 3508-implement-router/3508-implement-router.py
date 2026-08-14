class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.m = memoryLimit
        self.u = set()
        self.l = 0
        self.d = defaultdict(list)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        temp_p = (source, destination, timestamp)
        if temp_p in self.u:
            return False
        if self.l >= self.m:
            old = self.q.popleft()
            self.u.remove(old)
            self.d[old[1]].pop(0)
            self.l -= 1
        self.q.append(temp_p)
        self.u.add(temp_p)
        self.d[destination].append(timestamp)
        self.l += 1
        return True

    def forwardPacket(self) -> List[int]:
        if self.l == 0:
            return []
        self.l -= 1
        p = self.q.popleft()
        self.u.remove(p)
        self.d[p[1]].pop(0)
        return list(p)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return bisect_right(self.d[destination], endTime) - bisect_left(
            self.d[destination], startTime)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
