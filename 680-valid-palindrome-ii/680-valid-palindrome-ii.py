class Solution:

    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        l = 0
        r = len(s) - 1
        while l <= r:
            if l == r:
                return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            elif s[l] != s[r]:
                L = s[:l] + s[l + 1:]
                R = s[:r] + s[r + 1:]
                return L == L[::-1] or R == R[::-1]
        return False
