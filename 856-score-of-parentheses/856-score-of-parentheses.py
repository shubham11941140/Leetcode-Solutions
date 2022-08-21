class Solution:

    @staticmethod
    def check(s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            elif stack and i == ")":
                stack.pop()
        return not stack

    def scoreOfParentheses(self, s: str) -> int:
        if s == "()":
            return 1
        if len(s) > 2 and self.check(s[1:len(s) - 1]):
            return 2 * self.scoreOfParentheses(s[1:len(s) - 1])
        for i in range(1, len(s) - 1):
            if self.check(s[:i]) and self.check(s[i:]):
                return self.scoreOfParentheses(
                    s[:i]) + self.scoreOfParentheses(s[i:])
