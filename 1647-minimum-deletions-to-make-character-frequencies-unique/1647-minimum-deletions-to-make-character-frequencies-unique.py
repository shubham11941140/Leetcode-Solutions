from collections import Counter
class Solution:
    def minDeletions(self, s: str) -> int:
        c = Counter(s)
        print(c)
        l = c.values()
        print(l)
        s = sorted(l)
        print(s)
        if len(s) == len(set(s)):
            return 0
        i = 0
        ans = 0
        while i < len(s):
            if not s[i]:
                i += 1
            elif s.count(s[i]) == 1:
                i += 1
            else:
                s[i] -= 1
                ans += 1
        print(s, ans)
        return ans