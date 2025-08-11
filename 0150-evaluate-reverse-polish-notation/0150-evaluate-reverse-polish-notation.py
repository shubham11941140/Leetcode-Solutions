class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-*/":
                b = stack.pop()
                a = stack.pop()
                if i == "+":
                    stack.append(a + b)
                elif i == "-":
                    stack.append(a - b)
                elif i == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack.pop()
