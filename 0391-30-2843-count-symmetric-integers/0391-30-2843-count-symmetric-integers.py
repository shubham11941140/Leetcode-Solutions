class Solution:

    def countSymmetricIntegers(self, low: int, high: int) -> int:
        c = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 == 0 and sum([int(s[j]) for j in range(n // 2)]) == sum(
                [int(s[j]) for j in range(n // 2, n)]
            ):
                c += 1
        return c
