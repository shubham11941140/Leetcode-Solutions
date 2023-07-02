class Solution:
    
    
    def satisfy(self, a):
        b = [0] * self.n
        for i in a:
            b[i[0]] -= 1
            b[i[1]] += 1
        if b.count(0) == self.n:
            return len(a)
        return 0    
    
    def sub(self, req, idx, curr):
        if idx == self.r:
            c = self.satisfy(curr)
            self.m = max(self.m, c)
            return
        self.sub(req, idx + 1, curr + [req[idx]])
        self.sub(req, idx + 1, curr)
                                  
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.n = n
        self.r = len(requests)
        self.a = []
        self.m = 0
        self.sub(requests, 0, [])
        return self.m
            
            
        
   