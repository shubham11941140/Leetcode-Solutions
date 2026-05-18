class Solution:

    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(k + 1)]
        for p in piles:
            for i in range(k, 0, -1):
                s = 0
                for j in range(min(i, len(p))):
                    s += p[j]
                    dp[i] = max(dp[i], dp[i - j - 1] + s)
        return dp[k]
