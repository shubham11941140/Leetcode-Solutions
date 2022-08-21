class Solution:

    @staticmethod
    def minRemoveToMakeValid(s: str) -> str:
        os = []
        cs = []
        for i, item in enumerate(s):
            if item == "(":
                os.append(i)
            elif item == ")":
                if os:
                    os.pop()
                else:
                    cs.append(i)
        return "".join([s[i] for i in range(len(s)) if i not in os + cs])
