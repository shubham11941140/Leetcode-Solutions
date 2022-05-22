class Solution:
    
    
    def pall(self, s):
        return s == s[::-1]
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        c = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                #print(s[i:j])
                if self.pall(s[i:j]):
                    #print(14, s[i:j])
                    c += 1
        return c

        