class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        n = len(a)
        m = len(b)
        ca = [0] * 26
        cb = [0] * 26
        for ch in a:
            ca[ord(ch) - ord('a')] += 1
        for ch in b:
            cb[ord(ch) - ord('a')] += 1
        ans = 10**100
        for i in range(26):
            ans = min(ans, n - ca[i] + m - cb[i])
        for i in range(1, 26):
            ca[i] += ca[i - 1]
            cb[i] += cb[i - 1]
        for i in range(26):
            if i > 0:
                ans = min(ans, n - ca[i - 1] + cb[i - 1])
            if i < 25:
                ans = min(ans, ca[i] + m - cb[i])
        return ans        