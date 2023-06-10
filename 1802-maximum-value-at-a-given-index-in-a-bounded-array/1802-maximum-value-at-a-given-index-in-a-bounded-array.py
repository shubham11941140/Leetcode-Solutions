class Solution:
    
    def sn(self, r):
        return (r *(r + 1)) // 2
    
    def calc(self, m, ele):
        #print("M", m, ele)
        s = 0
        if ele >= m - 1:
            s = ((m * (m - 1)) // 2) + 1 * (ele - (m - 1))
        if ele < m - 1:
            rem = m - 1 - ele
            s = ((m * (m - 1)) // 2) - self.sn(rem)
        return s

    
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
                # call test
                if self.help(n, index, m + 1) > maxSum:
                    return m                
                l = m
        return 0
