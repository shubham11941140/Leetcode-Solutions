class Solution:                     
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[1 for i in range(n)] for j in range(m)]       
        
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1]
            
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                
        return dp[m - 1][n - 1]
        