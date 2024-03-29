class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if not k or n >= k + maxPts:
            return 1.0
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        window_sum = 1.0
        probability = 0.0
        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts
            if i < k:
                window_sum += dp[i]
            else:
                probability += dp[i]
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
        return probability
   