class Solution:

    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            minutes.append(h * 60 + m)

        # Sort the minutes
        minutes.sort()

        # Initialize the minimum difference to a large number
        min_diff = float("inf")

        # Find the minimum difference between consecutive times
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i - 1])

        # Check the difference between the first and last time points (circular difference)
        min_diff = min(min_diff, 1440 + minutes[0] - minutes[-1])

        return min_diff
