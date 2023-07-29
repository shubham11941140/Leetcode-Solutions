class Solution:

    def soupServings(self, n: int) -> float:
        N = n
        if N > 4800:
            return 1
        N = (N + 24) // 25
        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 0.5
        for i in range(1, N + 1):
            dp[i][0] = 0
            dp[0][i] = 1
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = 0.25 * (dp[max(i - 4, 0)][j] +
                                   dp[max(i - 3, 0)][max(j - 1, 0)] +
                                   dp[max(i - 2, 0)][max(j - 2, 0)] +
                                   dp[max(i - 1, 0)][max(j - 3, 0)])
        return dp[N][N]
