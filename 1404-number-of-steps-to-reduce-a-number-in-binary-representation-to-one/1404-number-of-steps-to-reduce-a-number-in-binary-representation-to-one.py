class Solution:
    def numSteps(self, s: str) -> int:
        n = int(s, 2)
        c = 0
        while n > 1:
            c += 1
            if n % 2:
                n += 1
            else:
                n //= 2
        return c
        
