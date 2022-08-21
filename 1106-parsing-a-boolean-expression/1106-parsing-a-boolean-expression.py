class Solution:    
    def parseBoolExpr(self, expression: str) -> bool:
        opst = []        
        bst = []
        for i, item in enumerate(expression):
            if item in ['!', '|', '&']:
                opst.append(item)
            elif item in ['(', 't', 'f']:
                if item == 't':
                    bst.append(True)
                elif item == 'f':
                    bst.append(False)                    
                else:
                    bst.append(item)
            elif item == ')':
                op = opst.pop()
                ans = True
                if op == '|':
                    ans = False
                    while bst[-1] != '(':
                        ans |= bst.pop()
                elif op == '&':
                    ans = True
                    while bst[-1] != '(':
                        ans &= bst.pop()                 
                elif op == '!':
                    while bst[-1] != '(':
                        ans = not bst.pop()
                bst.pop()
                bst.append(ans) 
        return bst[0]
