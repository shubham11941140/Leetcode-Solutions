class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum([(i + 1) * (123 - ord(s[i])) for i in range(len(s))])