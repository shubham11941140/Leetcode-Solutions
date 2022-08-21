class Solution:

    def check(self, a):
        h = list(set(a))
        for i, item in enumerate(h):
            if (item == item.lower() and item.upper() not in h) or (item == item.upper() and item.lower() not in h):
                return False
        return True

    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = -1
        for i in range(n):
            for j in range(i + 1, n + 1):
                if self.check(s[i:j]):
                    ans = max(ans, j - i + 1)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i + 1 == ans and self.check(s[i:j]):
                    return s[i:j]
        return ""
