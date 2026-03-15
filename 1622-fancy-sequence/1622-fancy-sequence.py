class Fancy:

    def __init__(self):
        self.m = 10**9 + 7  
        self.v = []  
        self.a = 1  
        self.b = 0  

    def append(self, val: int) -> None:
        x = (val - self.b + self.m) % self.m
        self.v.append(x * pow(self.a, self.m - 2, self.m) % self.m)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.m

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.m
        self.b = (self.b * m) % self.m

    def getIndex(self, idx: int) -> int:
        return -1 if idx >= len(self.v) else (self.a * self.v[idx] + self.b) % self.m

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)