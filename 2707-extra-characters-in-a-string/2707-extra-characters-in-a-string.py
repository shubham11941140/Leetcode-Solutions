class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s) + 1
        dp = [0] + [n] * (n - 1)
        word_set = set(dictionary)

        for i in range(1, n):
            dp[i] = dp[i - 1] + 1

            for length in range(1, i + 1):
                if s[i - length:i] in word_set:
                    dp[i] = min(dp[i], dp[i - length])

        return dp[-1]
