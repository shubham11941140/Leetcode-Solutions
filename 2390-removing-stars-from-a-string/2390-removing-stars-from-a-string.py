class Solution:

    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char != "*":
                stack.append(char)
            else:
                if stack[-1] and char == "*":
                    stack.pop()
        return "".join(char for char in stack)
