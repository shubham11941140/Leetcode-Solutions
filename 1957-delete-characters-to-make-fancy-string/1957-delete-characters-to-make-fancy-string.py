class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        count = 0
        for i, char in enumerate(s):
            if i > 1 and s[i] == s[i - 1] == s[i - 2]:
                continue
            result.append(char)
        return ''.join(result)
        