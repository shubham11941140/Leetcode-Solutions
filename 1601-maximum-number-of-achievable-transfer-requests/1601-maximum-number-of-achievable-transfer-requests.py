class Solution:
        
    def satisfy(self, a):
        b = [0] * self.n
        for i in a:
            b[i[0]] -= 1
            b[i[1]] += 1
        return len(a) if b.count(0) == self.n else 0
    
    def sub(self, idx, curr):
        if idx == self.r:
            c = self.satisfy(curr)
            self.m = max(self.m, c)
            return
        self.sub(idx + 1, curr + [self.req[idx]])
        self.sub(idx + 1, curr)
                                  
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        self.n = n
        self.r = len(requests)
        self.req = requests.copy()
        self.m = 0
        self.sub(0, [])
        return self.m
            
            
        
   