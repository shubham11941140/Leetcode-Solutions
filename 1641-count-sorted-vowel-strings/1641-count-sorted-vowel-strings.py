import random

class Solution:
    
    def __init__(self):
        self.c = 0
    
    def pall(self, a, b, k):
        if k == 0:
            self.c += 1
            #g = ''.join(b)
            #ans.append(g)
            return
        else:
            for i in a:
                if b:
                    if i >= b[-1]:
                        #print(14, i, b[-1])
                        self.pall(a, b + [i], k - 1)
                    else:
                        break
                else:
                    self.pall(a, b + [i], k - 1)
    
    
    def countVowelStrings(self, n: int) -> int:
        # Generate all 4 length strings
        a = ['a','e','i','o','u'][::-1]
        k = 50
        ans = []
        b = []
        self.pall(a, b, n)
        #print(ans)
        print(len(ans))
        print(self.c)
        return self.c
        final = []
        for i in ans:
            m = ''.join(sorted(i))
            if m not in final:
                final.append(m)
        #print(final)
        print(len(final))
        
        
        
        