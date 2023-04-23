class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        # dp[i] means the number of ways to restore s[i:]
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        mod = 10**9 + 7

        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                continue
            num = 0
            for j in range(i, len(s)):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[i] += dp[j + 1]
                dp[i] %= mod

        return dp[0]
