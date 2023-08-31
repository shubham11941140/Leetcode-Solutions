class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        inter = sorted([(max(0, i - ranges[i]), min(n, i + ranges[i])) for i in range(n + 1)])
        taps = 0  # Number of taps used
        current_end = 0  # The current rightmost point covered by taps
        i = 0

        while i <= n:
            # Find the farthest tap we can reach from the current position
            farthest = current_end

            while i <= n and inter[i][0] <= current_end:
                farthest = max(farthest, inter[i][1])
                i += 1

            # If we couldn't find a tap that covers the current position, return -1
            if farthest == current_end:
                return -1

            # Increment the taps count and update the current end
            taps += 1
            current_end = farthest

            # If we've covered the entire garden, return the taps count
            if current_end >= n:
                return taps

        return -1  # If we can't cover the entire garden

       