from collections import Counter


class Solution:

    def minDeletions(self, s: str) -> int:
        s = sorted(Counter(s).values())
        init = sum(s)
        n = len(s)
        i = 0
        while i < n:
            if not s[i] or s.count(s[i]) == 1:
                i += 1
            else:
                s[i] -= 1
        return init - sum(s)
