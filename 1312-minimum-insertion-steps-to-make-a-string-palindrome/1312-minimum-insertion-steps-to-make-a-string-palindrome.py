class Solution:

    def minInsertions(self, s: str) -> int:
        # reverse the string
        t = s[::-1]
        # find the length of the longest common subsequence
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # return the minimum number of insertions
        return n - dp[n][n]
