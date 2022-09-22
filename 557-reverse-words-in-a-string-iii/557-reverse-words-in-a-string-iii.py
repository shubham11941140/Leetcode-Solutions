class Solution:

    def reverseWords(self, s: str) -> str:
        res = ""
        for i in s.split():
            res += i[::-1] + " "
        return res[:-1]
