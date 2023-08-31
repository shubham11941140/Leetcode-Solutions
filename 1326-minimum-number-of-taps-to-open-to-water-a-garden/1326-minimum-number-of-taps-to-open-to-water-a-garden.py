class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inter = sorted([(max(0, i - ranges[i]), min(n, i + ranges[i])) for i in range(n + 1)])
        taps = 0  # Number of taps used
        ce = 0  # The current rightmost point covered by taps
        i = 0

        while i <= n:
            # Find the farthest tap we can reach from the current position
            f = ce

            while i <= n and inter[i][0] <= ce:
                f = max(f, inter[i][1])
                i += 1
            if f == ce:
                return -1
            taps += 1
            ce = f
            if ce >= n:
                return taps
        return -1
       