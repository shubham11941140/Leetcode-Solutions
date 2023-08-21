class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n):
            if not (n % i):
                t = s[:i]
                if t * (n // i) == s:
                    return True
        return False
