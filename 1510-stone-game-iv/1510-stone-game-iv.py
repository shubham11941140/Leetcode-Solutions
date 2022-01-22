from math import ceil, sqrt

class Solution:            
    def winnerSquareGame(self, n: int) -> bool:        
        a = [(i*i) for i in range(1, ceil(sqrt(n)) + 1)]
        k = len(a)
        dp = [False] * (n + 1)
        for i in range(n + 1):
            for j in range(k):
                val = i - a[j]
                if val < 0:
                    break
                if not dp[val]:
                    dp[i] = True
                    break
        return dp[n]    
        