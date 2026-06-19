class Solution:

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            # Initialize with the maximum steps (all 'Paste' operations)
            dp[i] = i
            for j in range(1, i // 2 + 1):
                if not (i % j):
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]
