from math import sqrt, floor
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = set([(i + 1) ** 2 for i in range(-1, floor(sqrt(c)))])
        for i in a:
            if c - i in a:
                return True
        return False
            
        