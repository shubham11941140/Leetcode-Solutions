class Solution:

    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        for right in range(len(s)):
            maxCost -= abs(ord(s[right]) - ord(t[right]))
            if maxCost < 0:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                left += 1
        return right - left + 1
