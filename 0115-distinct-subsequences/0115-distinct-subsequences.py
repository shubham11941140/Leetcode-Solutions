class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                dp[i][j] = dp[i + 1][j] + (dp[i + 1][j + 1] if s[i] == t[j] else 0)        
        return dp[0][0]