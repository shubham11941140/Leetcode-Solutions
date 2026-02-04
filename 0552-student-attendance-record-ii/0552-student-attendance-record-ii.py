class Solution:

    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0, 0, 0], [0, 0, 0]]
        dp[0][0] = 1

        for i in range(1, n + 1):
            new_dp = [[0, 0, 0], [0, 0, 0]]

            # Append 'P'
            for j in range(2):
                for k in range(3):
                    new_dp[j][0] = (new_dp[j][0] + dp[j][k]) % MOD

            # Append 'A'
            for k in range(3):
                new_dp[1][0] = (new_dp[1][0] + dp[0][k]) % MOD

            # Append 'L'
            for j in range(2):
                for k in range(1, 3):
                    new_dp[j][k] = (new_dp[j][k] + dp[j][k - 1]) % MOD

            dp = new_dp

        return sum(sum(dp[j]) for j in range(2)) % MOD
