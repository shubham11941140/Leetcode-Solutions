class Solution:

    @staticmethod
    def isPrefixString(s: str, words: List[str]) -> bool:
        check = ""
        for i in words:
            check += i
            if check == s:
                return True
        return False
