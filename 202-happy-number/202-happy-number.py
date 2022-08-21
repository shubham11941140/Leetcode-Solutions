class Solution:

    def rep(self, n):
        return sum([pow(int(i), 2) for i in str(n)])

    def isHappy(self, n: int) -> bool:
        for _ in range(1000):
            if n == 1:
                return True
            n = self.rep(n)
        return False
