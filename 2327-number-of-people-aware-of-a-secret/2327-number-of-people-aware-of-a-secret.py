class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        share = 0
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            if i - delay >= 0:
                share += dp[i - delay]
            if i - forget >= 0:
                share -= dp[i - forget]
            dp[i] = share
        return sum([dp[i]
                    for i in range(n - forget, n) if i >= 0]) % (10**9 + 7)
