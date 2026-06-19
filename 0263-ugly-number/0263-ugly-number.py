class Solution:

    def isUgly(self, n: int) -> bool:
        if not n:
            return False
        for i in [2, 3, 5]:
            while not (n % i):
                n //= i
        return n == 1
