class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(s):
            ctr = 0
            for i in s:
                if i == '(':
                    ctr += 1
                elif i == ")":
                    if ctr == 0:
                        return False
                    ctr -= 1            
            return not ctr        
        level = {s}
        while True:
            valid = list(filter(isValid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for i in range(len(s)) for s in level}