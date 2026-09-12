class Solution:

    def check(self, m, x):
        cnt = 0
        for i in range(self.lb):
            if self.b[i] <= x:
                cnt += 1
                if cnt == self.k:
                    m -= 1
                    cnt = 0
            else:
                cnt = 0
        return m <= 0

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        self.b = bloomDay
        self.k = k
        self.lb = len(bloomDay)
        if m * k > self.lb:
            return -1
        l = 1
        r = max(self.b)
        while l < r:
            mid = (l + r) // 2
            if self.check(m, mid):
                r = mid
            else:
                l = mid + 1
        return l
