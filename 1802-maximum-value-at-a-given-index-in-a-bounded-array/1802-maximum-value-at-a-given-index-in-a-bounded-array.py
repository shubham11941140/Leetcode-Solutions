class Solution:
    
    def sn(self, r):
        return (r * (r + 1)) // 2
    
    def calc(self, m, ele):
        if ele >= m - 1:
            return ((m * (m - 1)) // 2) + ele - m + 1
        else:
            return ((m * (m - 1)) // 2) - (((m - ele - 1) * (m - ele)) // 2)

    
    def help(self, n, idx, m):               
        return self.calc(m, idx) + self.calc(m, n - 1 - idx) + m

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        l = 1
        r = maxSum
        while l <= r:
            if r - l <= 100:
                for i in reversed(range(l, r + 1)):
                    if self.help(n, index, i) <= maxSum:
                        return i
            m = (l + r) // 2
            s = self.help(n, index, m)
            if s > maxSum:
                r = m
            if s <= maxSum:
                if self.help(n, index, m + 1) > maxSum:
                    return m                
                l = m
        return 0
