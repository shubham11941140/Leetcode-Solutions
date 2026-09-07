class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [1] * n
        result = 0
        for i in range(n):
            dp[i] += sum([dp[j] for j in range(i) if s[i] != s[j]])                    
            result += dp[i] % (10 ** 9 + 7)
        return result % (10 ** 9 + 7)