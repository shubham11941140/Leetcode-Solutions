class Solution:

    def __init__(self):
        self.d = [1000 for i in range(1015)]
        self.d[1] = 0
        for i in range(2, 1010):
            for j in range(2, i + 1):
                if i == j:
                    self.d[i] = min(self.d[i], i)
                if i % j == 0:
                    self.d[i] = min(self.d[i], self.d[j] + (i // j))

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            # Initialize with the maximum steps (all 'Paste' operations)
            dp[i] = i
            for j in range(1, i // 2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)

        return dp[n]
        return self.d[n]
