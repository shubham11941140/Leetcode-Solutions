class Solution:

    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        moves = [
            [4, 6],
            [6, 8],
            [7, 9],
            [4, 8],
            [3, 9, 0],
            [],
            [1, 7, 0],
            [2, 6],
            [1, 3],
            [2, 4],
        ]

        dp = [1] * 10
        for _ in range(n - 1):
            dp2 = [0] * 10
            for node in range(10):
                for nei in moves[node]:
                    dp2[nei] += dp[node]
                    dp2[nei]
            dp = dp2

        return sum(dp) % MOD
