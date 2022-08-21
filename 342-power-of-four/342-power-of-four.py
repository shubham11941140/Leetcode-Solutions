class Solution:

    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        if n <= 0:
            return False
        return 4**round(log(n, 4)) == n
