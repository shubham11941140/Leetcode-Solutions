class Solution:

    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num:
            c += 1
            if num % 2:
                num -= 1
            else:
                num //= 2
        return c
