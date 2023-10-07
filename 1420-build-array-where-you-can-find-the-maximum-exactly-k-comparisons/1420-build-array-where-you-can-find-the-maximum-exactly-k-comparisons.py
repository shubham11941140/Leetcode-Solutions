class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:        
        def dp(i, k, last, dct):
            if i == n:
                return int(not k)
            if (i, k, last) in dct:
                return dct[(i, k, last)]
            val = 0
            for j in range(1, m + 1):
                val += (dp(i + 1, k, last, dct) if j <= last else dp(i + 1, k - 1, j, dct))
            dct[(i, k, last)] = val
            return val        
        return dp(0, k, -1, {}) % (10 ** 9 + 7)
        