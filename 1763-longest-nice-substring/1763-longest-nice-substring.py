class Solution:

    def check(self, a):
        h = list(set(a))
        for i in range(len(h)):
            if (h[i] == h[i].lower() and h[i].upper() not in h) or (h[i] == h[i].upper() and h[i].lower() not in h):
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
