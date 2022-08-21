class Solution:

    @staticmethod
    def countVowelPermutation(n: int) -> int:
        M = 10**9 + 7
        dp = [[0 for i in range(5)] for i in range(n)]
        for j in range(5):
            dp[0][j] = 1
        for i in range(1, n):
            dp[i][0] = (dp[i][0] + dp[i - 1][1] + dp[i - 1][2] +
                        dp[i - 1][4]) % M
            dp[i][1] = (dp[i][1] + dp[i - 1][0] + dp[i - 1][2]) % M
            dp[i][2] = (dp[i][2] + dp[i - 1][1] + dp[i - 1][3]) % M
            dp[i][3] = (dp[i][3] + dp[i - 1][2]) % M
            dp[i][4] = (dp[i][4] + dp[i - 1][2] + dp[i - 1][3]) % M
        return sum(dp[n - 1]) % M
