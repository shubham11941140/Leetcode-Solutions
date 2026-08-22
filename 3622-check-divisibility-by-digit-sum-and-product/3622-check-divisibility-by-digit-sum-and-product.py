class Solution:
    def checkDivisibility(self, n: int) -> bool:
        v = [int(i) for i in str(n)]
        mv = 1
        for i in v:
            mv *= i
        return not (n % (sum(v) + mv))        