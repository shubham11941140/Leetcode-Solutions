from math import log


class Solution:

    @staticmethod
    def isPowerOfThree(n: int) -> bool:
        if n <= 0:
            return False
        return 3**round(log(n, 3)) == n
