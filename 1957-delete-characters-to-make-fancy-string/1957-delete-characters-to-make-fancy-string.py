class Solution:

    def makeFancyString(self, s: str) -> str:
        return "".join(
            [c for i, c in enumerate(s) if not (i > 1 and s[i] == s[i - 1] == s[i - 2])]
        )
