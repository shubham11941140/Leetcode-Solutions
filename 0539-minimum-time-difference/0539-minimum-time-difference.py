class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        m = []
        for time in timePoints:
            h, mi = map(int, time.split(":"))
            m.append(h * 60 + mi)
        m.sort()
        return min(
            min([m[i] - m[i - 1] for i in range(1, len(m))]), 1440 + m[0] - m[-1]
        )
