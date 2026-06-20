class Solution:
    def maxBuilding(self, num: int, r: list[list[int]]) -> int:
        r = sorted(r + [[1, 0]])
        n = len(r)

        def yCap(x1, y1, x2, y2):
            return min(y2, y1 + abs(x2 - x1))

        def yPeak(x1, y1, x2, y2):
            return (y1 + y2 + x2 - x1) >> 1
        
        for i in range(1, n):
            r[i][1] = yCap(*r[i - 1], *r[i])

        for i in range(n - 2, -1, -1):
            r[i][1] = yCap(*r[i + 1], *r[i])

        val = [yPeak(*r[i - 1], *r[i]) for i in range(1, n)]
        return max(max(val) if val else 0, r[-1][1] + num - r[-1][0])        