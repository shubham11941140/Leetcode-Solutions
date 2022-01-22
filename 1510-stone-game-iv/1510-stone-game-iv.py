from math import ceil, sqrt

class Solution:        
    
    def isperfectsquare(self, n):
        return pow(int(sqrt(n)), 2) == n
    
    def winnerSquareGame(self, n: int) -> bool:        
        # generate sqaures till n
        a = [(i*i) for i in range(1, ceil(sqrt(n)) + 1)]
        k = len(a)
        
        # dp table will store numbers
        dp = [False] * (n + 1)
        # Base case
        dp[0] = False
        
        # DP case
        for i in range(n + 1):
            '''
            for j in range(i):
                if not dp[j]:
                    if self.isperfectsquare(i - j):
                        dp[i] = True
                        break
            '''
            for j in range(k):
                # take diff of pes
                val = i - a[j] # diff is ps
                if val < 0:
                    break
                if not dp[val]:
                    dp[i] = True
                    break
            

        print(dp)
        return dp[n]    
        