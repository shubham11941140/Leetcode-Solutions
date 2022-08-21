class Solution:

    @staticmethod
    def numberOfSteps(num: int) -> int:
        c = 0
        while num:
            c += 1
            if num % 2:
                num -= 1
            else:
                num //= 2
        return c
