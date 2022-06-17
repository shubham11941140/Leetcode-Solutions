class Solution:
    def largestOddNumber(self, num: str) -> str:
        f = False
        for i in num:
            if int(i) % 2:
                f = True
                break
        if not f:
            return ""
        for i in reversed(range(len(num))):
            if int(num[i]) % 2:
                # Mark i
                return num[:i + 1]
            
        