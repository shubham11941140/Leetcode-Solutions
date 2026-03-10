class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # base: only zeros
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1

        # base: only ones
        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        for i in range(zero + 1):
            for j in range(one + 1):
                if i == 0 and j == 0:
                    continue

                if i > 0 and j > 0:
                    dp0[i][j] = dp0[i - 1][j] + dp1[i - 1][j]
                    if i - limit - 1 >= 0:
                        dp0[i][j] -= dp1[i - limit - 1][j]

                    dp1[i][j] = dp1[i][j - 1] + dp0[i][j - 1]
                    if j - limit - 1 >= 0:
                        dp1[i][j] -= dp0[i][j - limit - 1]

        return (dp0[zero][one] + dp1[zero][one]) % (10 ** 9 + 7)        