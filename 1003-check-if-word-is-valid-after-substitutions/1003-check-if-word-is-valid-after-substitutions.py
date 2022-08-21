class Solution:

    @staticmethod
    def isValid(s: str) -> bool:
        while "abc" in s:
            s = s.replace("abc", "")
        return s == ""
