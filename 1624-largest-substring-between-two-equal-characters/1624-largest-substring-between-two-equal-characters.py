class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}
        max_length = -1

        for i in range(len(s)):
            if s[i] in first_occurrence:
                max_length = max(max_length, i - first_occurrence[s[i]] - 1)
            else:
                first_occurrence[s[i]] = i

        return max_length        