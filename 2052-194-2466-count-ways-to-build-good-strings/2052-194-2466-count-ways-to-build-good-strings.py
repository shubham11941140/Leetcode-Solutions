class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        mod = 10**9 + 7
        @lru_cache(None)
        def do(n):
            if n == 0:
                return 1
            elif n < 0:
                return 0
            return (do(n-one) + do(n-zero)) % mod
        return sum(do(x) for x in range(low, high+1))%mod        