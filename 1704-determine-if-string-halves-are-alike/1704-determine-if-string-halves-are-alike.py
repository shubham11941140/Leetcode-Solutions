class Solution:

    def halvesAreAlike(self, s: str) -> bool:
        a = 0
        n = len(s)
        for i in range(n // 2):
            if s[i] in "aeiouAEIOU":
                a += 1
            if s[n // 2 + i] in "aeiouAEIOU":
                a -= 1
        return a == 0
