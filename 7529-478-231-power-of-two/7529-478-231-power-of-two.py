from math import log2


class Solution:

    def isPowerOfTwo(self, n: int) -> bool:
        return False if n <= 0 else 2**int(log2(n)) == n
