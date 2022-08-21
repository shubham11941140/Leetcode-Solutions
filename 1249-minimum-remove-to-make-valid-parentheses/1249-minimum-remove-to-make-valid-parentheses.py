class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:
        os = []
        cs = []
        for i in range(len(s)):
            if s[i] == "(":
                os.append(i)
            elif s[i] == ")":
                if os:
                    os.pop()
                else:
                    cs.append(i)
        return "".join([s[i] for i in range(len(s)) if i not in os + cs])
