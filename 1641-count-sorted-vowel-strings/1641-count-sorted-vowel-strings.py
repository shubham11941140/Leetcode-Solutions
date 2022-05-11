class Solution:
    
    def __init__(self):
        self.c = 0
    
    def pall(self, a, b, k):
        if not k:
            self.c += 1
            return
        else:
            for i in a:
                if b != -1:
                    if i < b:
                        break
                    else:
                        self.pall(a, i, k - 1)
                else:
                    self.pall(a, i, k - 1)
    
    
    def countVowelStrings(self, n: int) -> int:
        a = ['a','e','i','o','u'][::-1]
        self.pall(a, -1, n)
        return self.c
        
        
        
        