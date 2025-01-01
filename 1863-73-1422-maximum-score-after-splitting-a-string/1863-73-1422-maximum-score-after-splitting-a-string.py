class Solution:
    def maxScore(self, s: str) -> int:
        o = s.count('1')
        m = 0
        for c in s[:-1]:
            o = (o - 1 if c == '1' else o + 1)
            m = max(m, o)
        return m