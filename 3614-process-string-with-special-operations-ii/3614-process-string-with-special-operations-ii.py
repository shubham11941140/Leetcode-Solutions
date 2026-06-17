class Solution:
    def processStr(self, s: str, k: int) -> str:
        L = 0
        for char in s:
            if 'a' <= char <= 'z': 
                L += 1
            elif char == '*': 
                L = max(0, L - 1)
            elif char == '#': 
                L *= 2            
        # Deterministic check for signal availability
        if k < 0 or k >= L: 
            return '.'
        rev = False
        for char in reversed(s):
            if char == '%':
                rev = not rev
                k = (L - 1 - k)
            elif char == '#':
                L //= 2
                if k >= L: 
                    k -= L
            elif char == '*':
                # Insertion transformation (Inverse Deletion)
                L += 1
            elif 'a' <= char <= 'z':
                # Signal capture: at this coordinate, does the signal resolve?
                # The 'rev' state determines our current vector basis.
                if k == L - 1: 
                    return char
                L -= 1        
        return '.'