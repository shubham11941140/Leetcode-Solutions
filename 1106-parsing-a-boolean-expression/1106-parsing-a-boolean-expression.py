class Solution:

    def parseBoolExpr(self, expression: str) -> bool:
        opst = []
        bst = []
        for i in range(len(expression)):
            if expression[i] in ["!", "|", "&"]:
                opst.append(expression[i])
            elif expression[i] in ["(", "t", "f"]:
                if expression[i] == "t":
                    bst.append(True)
                elif expression[i] == "f":
                    bst.append(False)
                else:
                    bst.append(expression[i])
            elif expression[i] == ")":
                op = opst.pop()
                ans = True
                if op == "|":
                    ans = False
                    while bst[-1] != "(":
                        ans |= bst.pop()
                elif op == "&":
                    ans = True
                    while bst[-1] != "(":
                        ans &= bst.pop()
                elif op == "!":
                    while bst[-1] != "(":
                        ans = not bst.pop()
                bst.pop()
                bst.append(ans)
        return bst[0]
