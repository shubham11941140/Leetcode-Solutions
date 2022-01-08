   
class Solution:
   
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:            
        m = len(s)
        dp = [False] * (m + 1)
        dp[0] = True
        for i in range(1, m + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
        return dp[m]
        

        