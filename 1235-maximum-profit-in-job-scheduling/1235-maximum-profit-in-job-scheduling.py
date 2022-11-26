class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        arr = sorted(zip(startTime, endTime, profit), key = lambda x: x[1])
        dp = [0] * n
        dp[0] = arr[0][2]
        for i in range(1, n):
            dp[i] = max(dp[i - 1], arr[i][2])
            for j in reversed(range(i)):
                if arr[j][1] <= arr[i][0]:
                    dp[i] = max(dp[i], dp[j] + arr[i][2])
                    break
        return dp[-1] 