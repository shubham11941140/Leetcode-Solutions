class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        return sum([len(set(s[s.find(c) + 1 : s.rfind(c)])) for c in set(s)])