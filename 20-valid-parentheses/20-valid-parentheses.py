class Solution:

    @staticmethod
    def isValid(s: str) -> bool:
        while s:
            t = s
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            if s == t:
                break
        return s == ""
