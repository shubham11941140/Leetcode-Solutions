class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return False if n <= 0 else 4 ** round(log(n, 4)) == n
