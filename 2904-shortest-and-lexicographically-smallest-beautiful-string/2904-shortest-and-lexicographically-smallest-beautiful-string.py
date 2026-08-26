class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        positions = [i for i, ch in enumerate(s) if ch == '1']
        if len(positions) < k:
            return ""
        ans = ""
        for i in range(len(positions) - k + 1):
            start = positions[i]
            end = positions[i + k - 1]
            candidate = s[start:end + 1]
            if not ans or len(candidate) < len(ans):
                ans = candidate
            elif len(candidate) == len(ans) and candidate < ans:
                ans = candidate
        return ans