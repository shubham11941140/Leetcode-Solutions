class Solution:

    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(words), len(words[0])
        dp = [0] * (len(target) + 1)
        dp[0] = 1
        for i in range(n):
            cnt = Counter([word[i] for word in words])
            for j in reversed(range(len(target))):
                dp[j + 1] += dp[j] * cnt[target[j]] % (10**9 + 7)
        return dp[-1] % (10**9 + 7)
