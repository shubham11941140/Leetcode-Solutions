from collections import Counter


class Solution:

    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        n = len(s)
        for i in range(n):
            if c[s[i]] == 1:
                return i
        return -1
