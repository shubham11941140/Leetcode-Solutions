class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            i = s.find(c)
            j = s.rfind(c)
            res += len(set(s[i + 1 : j]))
        return res
