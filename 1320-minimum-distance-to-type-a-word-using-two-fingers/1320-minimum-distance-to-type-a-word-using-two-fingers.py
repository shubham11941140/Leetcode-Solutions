class Solution:
    def minimumDistance(self, word: str) -> int:
        def cal(a, b):
            return abs(a // 6 - b // 6) + abs(a % 6 - b % 6)
        n = len(word)
        dp = [[[0] * 26 for _ in range(26)] for _ in range(n + 1)]

        for i in range(n):
            t = ord(word[i]) - ord('A')

            for j in range(26):
                for k in range(26):
                    dp[i + 1][j][k] = 1000000

            for j in range(26):
                for k in range(26):
                    dp[i + 1][j][t] = min(dp[i + 1][j][t], dp[i][j][k] + cal(k, t))
                    dp[i + 1][t][k] = min(dp[i + 1][t][k], dp[i][j][k] + cal(j, t))

        return min([dp[n][j][k] for j in range(26) for k in range(26)])