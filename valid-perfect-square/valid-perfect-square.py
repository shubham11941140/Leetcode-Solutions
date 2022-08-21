from math import sqrt, floor
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return pow(floor(sqrt(num)), 2) == num

