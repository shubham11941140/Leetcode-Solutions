class Solution:

    def isPalindrome(self, s: str) -> bool:
        t = list(s)
        k = [t[i].lower() for i in range(len(t)) if t[i].isalnum()]
        return k == k[::-1]
