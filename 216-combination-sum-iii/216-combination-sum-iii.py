class Solution:
    
    def __init__(self):
        self.a = list(range(1, 10))
        self.ans = []
    
    def rec(self, k, n, b):
        if not k and not n:
            self.ans.append(b.copy())
        for i in self.a:
            if i not in b:
                if i > n:
                    break
                else:
                    self.rec(k - 1, n - i, b + [i])                
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        b = []
        ans = []
        self.rec(k, n, b)
        c = []
        for i in self.ans:
            l = sorted(i)
            if l not in c:
                c.append(l)
        return c
                
        
        