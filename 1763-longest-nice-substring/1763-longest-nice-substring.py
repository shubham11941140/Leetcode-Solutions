class Solution:
    
    def check(self, a):
        f = True
        h = list(set(a))
        
        for i in range(len(h)):
            if a == "aAa":
                print(6, h[i])
            if h[i] == h[i].lower() and h[i].upper() not in h:
                f = False
            elif h[i] == h[i].upper() and h[i].lower() not in h:
                f = False
        return f
                
                
    
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = -1
        for i in range(n):
            for j in range(i + 1, n + 1):
                print("S", s[i:j])
                if self.check(s[i:j]):
                    ans = max(ans, j - i + 1)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if j - i + 1 == ans and self.check(s[i:j]):
                    return s[i:j]
                    #ans = max(ans, j - i + 1)                    
        #return ans
        return ""
        