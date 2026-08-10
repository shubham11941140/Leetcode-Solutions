class Solution:            
    def winnerSquareGame(self, n: int) -> bool:        
        a = [(i * i) for i in range(1, ceil(sqrt(n)) + 1)]
        k = len(a)
        dp = [False] * (n + 1)
        for i in range(n + 1):
            for j in range(k):
                if i < a[j]:
                    break
                if not dp[i - a[j]]:
                    dp[i] = True
                    break
        return dp[n]        