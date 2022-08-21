class Solution:

    @staticmethod
    def addDigits(num: int) -> int:
        while num > 9:
            num = sum([int(i) for i in str(num)])
        return num
