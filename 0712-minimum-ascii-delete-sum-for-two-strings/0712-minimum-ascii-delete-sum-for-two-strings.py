class Solution:

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # Create a 2D DP table with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill the first row and first column of DP table
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        # Fill the DP table using recurrence relation
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]),
                                   dp[i][j - 1] + ord(s2[j - 1]))

        # The answer will be in the bottom-right cell of the DP table
        return dp[m][n]
