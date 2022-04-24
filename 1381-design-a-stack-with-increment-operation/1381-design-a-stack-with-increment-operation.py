class CustomStack:

    def __init__(self, maxSize: int):
        self.s = []
        self.l = 0
        self.m = maxSize
        
    def push(self, x: int) -> None:
        if self.l < self.m:
            self.s.append(x)
            self.l += 1

    def pop(self) -> int:
        if self.l:
            val = self.s.pop()
            self.l -= 1
            return val
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.l > k:
            for i in range(k):
                self.s[i] += val
        else:
            for i in range(self.l):
                self.s[i] += val
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)