class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        L = goal
        N = n
        K = k
        dp = [[0] * (L + 1) for _ in range(N + 1)]
        dp[0][0] = 1
        for i in range(1, N + 1):
            for j in range(1, L + 1):
                dp[i][j] += dp[i - 1][j - 1] * (N - i + 1)
                dp[i][j] += dp[i][j - 1] * max(i - K, 0)
                dp[i][j] %= 10**9 + 7
        return dp[N][L]        