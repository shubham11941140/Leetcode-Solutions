class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = list(str(x))
        return c == c[::-1]
        