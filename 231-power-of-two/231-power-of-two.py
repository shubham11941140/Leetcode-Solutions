from math import log2


class Solution:

    @staticmethod
    def isPowerOfTwo(n: int) -> bool:
        if n <= 0:
            return False
        return 2**int(log2(n)) == n
