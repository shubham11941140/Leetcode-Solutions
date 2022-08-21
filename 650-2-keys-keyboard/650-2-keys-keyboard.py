class Solution:
    
    def factor(self, n):
        for i in range(2, n + 1):
            if n % i == 0:
                return i

    def minSteps(self, n: int) -> int:
        
        dp = [1000 for i in range(2000)]
        dp[1] = 0
        for i in range(2, 1050):
            for j in range(2, i + 1):
                if i == j:
                    dp[i] = min(dp[i], i)
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + 1 + (i // j) - 1)
        print(dp)
        return dp[n]
        
            
        
