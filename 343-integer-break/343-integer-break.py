class Solution:
    def integerBreak(self, n: int) -> int:
        # Break into positive integers
        dp = [0 for i in range(60)]
        dp[1] = 1
        for i in range(2, 60):
            ans = 0
            for j in range(i):
                p = max(j, dp[j])
                q = max(i - j, dp[i - j])
                ans = max(ans, p * q)
            dp[i] = ans
        print(dp)
        return dp[n]
        
        