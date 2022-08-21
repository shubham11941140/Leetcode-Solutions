class Solution:

    @staticmethod
    def isPalindrome(x: int) -> bool:
        c = list(str(x))
        return c == c[::-1]
