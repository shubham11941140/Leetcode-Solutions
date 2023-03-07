class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t):
            return sum([t // i for i in time]) >= totalTrips
        l, r = 0, 10 ** 18
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l        