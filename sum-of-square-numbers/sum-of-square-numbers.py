from math import floor, sqrt


class Solution:

    @staticmethod
    def judgeSquareSum(c: int) -> bool:
        a = {(i + 1)**2 for i in range(-1, floor(sqrt(c)))}
        for i in a:
            if c - i in a:
                return True
        return False
