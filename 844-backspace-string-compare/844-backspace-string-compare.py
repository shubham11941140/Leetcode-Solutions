class Solution:    

    def change(self, s):
        stack = []
        for i in s:
            if i == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.change(s) == self.change(t)




