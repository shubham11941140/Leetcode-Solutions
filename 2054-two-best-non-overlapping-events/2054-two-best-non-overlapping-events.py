class Solution:

    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        # dp array to store the maximum value from the end to the current position
        dp = [0] * (n + 1)
        max_value = 0
        for i in range(n - 1, -1, -1):
            max_value = max(max_value, events[i][2])
            dp[i] = max_value
        result = 0
        for i in range(n):
            start, end, value = events[i]
            left, right = i + 1, n
            while left < right:
                mid = (left + right) // 2
                if events[mid][0] > end:
                    right = mid
                else:
                    left = mid + 1
            if left < n:
                result = max(result, value + dp[left])
            else:
                result = max(result, value)
        return result
