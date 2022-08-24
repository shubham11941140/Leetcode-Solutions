class Solution:

    def subset(self, temp, idx):
        if idx == self.n:
            self.ans.add(temp)
            return
        self.subset(temp + self.a[idx], idx + 1)
        self.subset(temp, idx + 1)               
    
    def checkPowersOfThree(self, n: int) -> bool:
        x = 1
        self.a = []
        while x <= 10 ** 7:
            self.a.append(x)
            x *= 3
        temp = 0
        idx = 0
        self.n = len(self.a)
        self.ans = set()
        self.subset(temp, idx)
        return n in self.ans