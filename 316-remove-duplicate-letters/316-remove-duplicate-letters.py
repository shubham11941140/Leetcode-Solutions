class Solution:                          
    
    def removeDuplicateLetters(self, s: str) -> str:
        # Check last occurrence of char
        stack = []
        last = {}
        for i, item in enumerate(s):
            last[item] = i
        for i, item in enumerate(s):
            if item not in stack:                
                while stack and item < stack[-1] and last[stack[-1]] > i:
                    stack.pop()                
                stack.append(item)                
        return ''.join(stack)
        
        
        