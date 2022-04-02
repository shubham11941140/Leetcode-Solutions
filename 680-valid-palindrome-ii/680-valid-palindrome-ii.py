class Solution:
    
    def palli(self, s):
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        if self.palli(s):
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
                return self.palli(L) or self.palli(R)
        return False
        