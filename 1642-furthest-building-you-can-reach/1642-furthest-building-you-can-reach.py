class Solution:
    
    def generate(self, a):
        return [(a[i + 1] - a[i]) for i in range(len(a) - 1) if a[i + 1] > a[i]]
    
    def valid(self, idx): 
        p = sorted(self.generate(self.h[:idx]))
        return self.b >= sum([p[i] for i in range(len(p) - self.l)])            
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        self.h = heights
        self.b = bricks
        self.l = ladders
        self.n = len(self.h)
        l = 0
        r = self.n - 1
        if self.valid(self.n):
            return r
        while l <= r:
            m = (l + r) // 2
            if self.valid(m):
                if not self.valid(m + 1):
                    return m - 1
                l = m + 1
            else:
                r = m - 1
     