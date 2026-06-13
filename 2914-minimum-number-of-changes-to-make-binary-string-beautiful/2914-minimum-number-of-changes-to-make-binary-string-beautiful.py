class Solution:

    def minChanges(self, s: str) -> int:
        return len([1 for i in range(0, len(s), 2) if s[i] != s[i + 1]])
