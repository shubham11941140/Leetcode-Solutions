from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        l = c.values()
        s = sorted(l)
        if len(s) == len(set(s)):
            return 0
        i = 0
        ans = 0
        while i < len(s):
            if not s[i] or s.count(s[i]) == 1:
                i += 1
            else:
                s[i] -= 1
                ans += 1
        return ans