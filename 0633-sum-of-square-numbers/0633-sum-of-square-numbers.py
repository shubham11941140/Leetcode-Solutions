class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = set([i ** 2 for i in range(ceil(sqrt(c)) + 1)])
        for i in a:
            if c - i in a:
                return True
        return False