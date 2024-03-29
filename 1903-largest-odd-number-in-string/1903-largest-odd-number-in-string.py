class Solution:

    @staticmethod
    def largestOddNumber(num: str) -> str:
        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                return num[:i + 1]
        return ""
