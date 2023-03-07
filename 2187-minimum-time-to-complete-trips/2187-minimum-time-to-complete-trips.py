class Solution:

    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def check(t):
            trips = 0
            for i in range(len(time)):
                trips += t // time[i]
            return trips >= totalTrips

        l, r = 0, 10**18
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l
