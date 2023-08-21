class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n):            
            if n % i == 0:
                #print(i, s[:i])
                t = s[:i]
                r = n // i
                #print(t * r)
                if t * r == s:
                    return True
        return False
        