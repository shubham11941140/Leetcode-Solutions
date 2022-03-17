class Solution:
    
    def check(self, s):
        stack = []
        for i in s:
            if i == '(':
                stack.append(i)
            elif stack and i == ')':
                stack.pop()
        return not stack
            
    def score(self, s):
        
        if s == "":
            return 0
        
        if s == "()":
            return 1
        
        if len(s) > 2 and self.check(s[1:len(s) - 1]):
            return 2 * self.score(s[1:len(s) - 1])
        
        else:
            # FInd the balance point
            for i in range(1, len(s) - 1):
                if self.check(s[:i]) and self.check(s[i:]):
                    print(i)
                    return self.score(s[:i]) + self.score(s[i:])
 

    
    def scoreOfParentheses(self, s: str) -> int:
        #print(s[len(s) - 2:], s[:len(s) - 2])
        return self.score(s)
        