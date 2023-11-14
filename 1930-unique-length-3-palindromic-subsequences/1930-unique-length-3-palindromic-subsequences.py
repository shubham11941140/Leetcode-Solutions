class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        for c in set(s):
            res += len(set(s[s.find(c) + 1 : s.rfind(c)]))
        return res        