class Solution:

    def makeFancyString(self, s: str) -> str:
        result = []
        for i, char in enumerate(s):
            if not (i > 1 and s[i] == s[i - 1] == s[i - 2]):
                result.append(char)
        return "".join(result)
