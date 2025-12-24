class Solution:

    def subtractProductAndSum(self, n: int) -> int:
        a = [int(i) for i in str(n)]
        p = 1
        for i in a:
            p *= i
        return p - sum(a)
