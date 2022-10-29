class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        b = bloomDay
        if m * k > len(b):
            return -1
        def check(m, x):
            cnt = 0
            for i in range(len(b)):
                if b[i] <= x:
                    cnt += 1
                    if cnt == k:
                        m -= 1
                        cnt = 0
                else:
                    cnt = 0
            return m <= 0
        l = 1
        r = max(b)
        while l < r:
            mid = (l + r) // 2
            if check(m, mid):
                r = mid
            else:
                l = mid + 1
        return l         