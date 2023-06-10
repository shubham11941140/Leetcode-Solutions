class Solution:
     
    def calc(self, m, e):
        return ((m * (m - 1)) // 2) + e - m + 1 if e >= m - 1 else ((m * (m - 1)) // 2) - (((m - e - 1) * (m - e)) // 2)
               
    def help(self, m):               
        return self.calc(m, self.i) + self.calc(m, self.n - 1 - self.i) + m

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum
        self.n = n
        self.i = index
        while l <= r:
            if r - l <= 100:
                for i in reversed(range(l, r + 1)):
                    if self.help(i) <= maxSum:
                        return i
            m = (l + r) // 2
            s = self.help(m)
            if s > maxSum:
                r = m
            if s <= maxSum:
                if self.help(m + 1) > maxSum:
                    return m                
                l = m
        return 0
