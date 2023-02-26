class Solution:
    def minDistance(self, word1: str, word2: str) -> int:        
        m = len(word1)
        n = len(word2)        
        if not m or not n:
            return max(m, n)      
        if m == 1 and n == 1:
            return int(word1 != word2)               
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]        
        for j in range(n + 1):
            dp[0][j] = j            
        for i in range(m + 1):
            dp[i][0] = i            
        for i in range(1, m + 1):
            for j in range(1, n + 1):            
                dp[i][j] = dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])                    
        return dp[m][n]
        