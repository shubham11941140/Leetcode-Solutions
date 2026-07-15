class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        so = n * (n - 2)
        se = n * (n - 1)
        return gcd(so, se)