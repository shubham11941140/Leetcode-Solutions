class Solution:

    def minTaps(self, n: int, ranges: List[int]) -> int:
        inter = sorted([(max(0, i - ranges[i]), min(n, i + ranges[i]))
                        for i in range(n + 1)])
        taps = 0  # Number of taps used
        ce = 0  # The current rightmost point covered by taps
        i = 0

        while i <= n:
            # Find the farthest tap we can reach from the current position
            farthest = ce

            while i <= n and inter[i][0] <= ce:
                farthest = max(farthest, inter[i][1])
                i += 1

            # If we couldn't find a tap that covers the current position, return -1
            if farthest == ce:
                return -1

            # Increment the taps count and update the current end
            taps += 1
            ce = farthest
            if ce >= n:
                return taps

        return -1  # If we can't cover the entire garden
