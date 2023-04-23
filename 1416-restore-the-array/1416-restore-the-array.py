class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * n + [1]
        for i in reversed(range(n)):
            if s[i] == "0":
                continue
            num = 0
            for j in range(i, n):
                num = num * 10 + int(s[j])
                if num > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % (10**9 + 7)
        return dp[0]
