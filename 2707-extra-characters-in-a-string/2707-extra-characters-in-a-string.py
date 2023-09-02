class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s) + 1
        dp = [0] + [n] * (n - 1)        
        w = set(dictionary)        
        for i in range(1, n):
            dp[i] = dp[i - 1] + 1
            
            for l in range(1, i + 1):
                if s[i - l:i] in w:
                    dp[i] = min(dp[i], dp[i - l])
                    
        return dp[-1]
