class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return False if n <= 0 else 3 ** round(log(n, 3)) == n