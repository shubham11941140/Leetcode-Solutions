class Solution:
    
    
    def change(self, s):
        stack = []
        for i in s:
            if i == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        print(stack)
        return stack
    
    
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Solve using stack
        return self.change(s) == self.change(t)
        
                
                
        