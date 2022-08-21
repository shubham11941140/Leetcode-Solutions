from math import floor, sqrt


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        return pow(floor(sqrt(num)), 2) == num
