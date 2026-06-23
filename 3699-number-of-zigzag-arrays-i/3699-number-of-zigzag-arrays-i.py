class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        m = r - l + 1
        dp = [1] * m
        for i in range(1, n):
            new_dp = [0] * m
            total = 0
            if i & 1:
                for j in reversed(range(m)):
                    new_dp[j] = total
                    total += dp[j]
            else:
                for j in range(m):
                    new_dp[j] = total
                    total += dp[j]
            dp = new_dp
        return (2 * sum(dp)) % (10 ** 9 + 7)