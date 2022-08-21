class Solution:

    def freq(self, a):
        d = dict()
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        return d

    def deleteAndEarn(self, nums: List[int]) -> int:
        f = self.freq(nums)
        # For spaced points there is no problem
        # Issue is with continuous streams
        # Solved using DP -> Pick and Not Pick best case
        s = sorted(list(set(nums)))
        n = len(s)
        dp = [0] * n

        if n == 1:
            return sum(nums)

        dp[0] = s[0] * f[s[0]]

        if s[0] + 1 == s[1]:
            dp[1] = max(dp[0], s[1] * f[s[1]])
        else:
            dp[1] = dp[0] + s[1] * f[s[1]]

        for i in range(2, n):
            if s[i] == s[i - 1] + 1:
                dp[i] = max(dp[i - 1], s[i] * f[s[i]] + dp[i - 2])
            else:
                dp[i] = s[i] * f[s[i]] + dp[i - 1]
        return dp[n - 1]
