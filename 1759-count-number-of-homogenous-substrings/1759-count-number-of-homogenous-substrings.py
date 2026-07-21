class Solution:
    def countHomogenous(self, s: str) -> int:
        res = i = 0
        for j in range(len(s)):
            if s[i] != s[j]:
                i = j
            res += j - i + 1
        return res % (10**9 + 7)
