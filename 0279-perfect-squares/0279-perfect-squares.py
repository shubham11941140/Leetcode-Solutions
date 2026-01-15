from math import ceil, sqrt


class Solution:

    def numSquares(self, n: int) -> int:
        gen = [(i * i) for i in range(1, 110)]
        k = len(gen)
        dp = [10**5 for i in range(n + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(k):
                if i < gen[j]:
                    break
                dp[i] = min(dp[i], dp[i - gen[j]] + 1)
        return dp[n]
