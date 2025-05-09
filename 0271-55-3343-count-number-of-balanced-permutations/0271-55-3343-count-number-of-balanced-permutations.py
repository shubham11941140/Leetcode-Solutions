class Solution:

    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        digit_values = [int(c) for c in num]
        total_sum = sum(digit_values)

        if total_sum % 2 == 1:
            return 0

        fact = [1] * (n + 1)
        inv = [1] * (n + 1)
        invFact = [1] * (n + 1)

        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD

        for i in range(2, n + 1):
            inv[i] = MOD - MOD // i * inv[MOD % i] % MOD

        for i in range(1, n + 1):
            invFact[i] = invFact[i - 1] * inv[i] % MOD

        half_sum = total_sum // 2
        half_len = n // 2

        dp = [[0] * (half_len + 1) for _ in range(half_sum + 1)]
        dp[0][0] = 1

        digit_count = [0] * 10
        for d in digit_values:
            digit_count[d] += 1
            for s in range(half_sum, d - 1, -1):
                for l in range(half_len, 0, -1):
                    dp[s][l] = (dp[s][l] + dp[s - d][l - 1]) % MOD

        res = dp[half_sum][half_len] * fact[half_len] * fact[n - half_len]

        for cnt in digit_count:
            res = res * invFact[cnt] % MOD

        return res
