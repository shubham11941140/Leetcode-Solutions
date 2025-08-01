class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7
        if not word:
            return 0

        groups = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count)

        total = 1
        for num in groups:
            total = (total * num) % MOD

        if k <= len(groups):
            return total

        dp = [0] * k
        dp[0] = 1

        for num in groups:
            new_dp = [0] * k
            sum_val = 0
            for s in range(k):
                if s > 0:
                    sum_val += dp[s - 1]
                if s > num:
                    sum_val -= dp[s - num - 1]
                new_dp[s] = sum_val % MOD
            dp = new_dp
        return (total - sum(dp[len(groups):k]) % MOD + MOD) % MOD        