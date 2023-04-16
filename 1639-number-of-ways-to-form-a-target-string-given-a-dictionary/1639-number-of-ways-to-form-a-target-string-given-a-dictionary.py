class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        mod = 10**9 + 7
        m, n = len(words), len(words[0])
        dp = [0] * (len(target) + 1)
        dp[0] = 1
        for i in range(n):
            cnt = collections.Counter([word[i] for word in words])
            for j in range(len(target) - 1, -1, -1):
                dp[j + 1] += dp[j] * cnt[target[j]] % mod
        return dp[-1] % mod
