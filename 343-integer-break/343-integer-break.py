class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n + 1)]
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = max([max(j, dp[j]) * max(i - j, dp[i - j]) for j in range(i)])
        return dp[n]
        
        