class Solution:

    def sub(self, s, a, b, idx):
        if idx >= 17:
            return
        s.append(a)
        self.sub(s, a + b[idx], b, idx + 1)
        self.sub(s, a, b, idx + 1)

    def checkPowersOfThree(self, n: int) -> bool:
        c = []    
        self.sub(c, 0, [3 ** i for i in range(17)], 0)
        return n in c
        