class Solution:
    
    def generate(self, a):
        return [(a[i + 1] - a[i]) for i in range(len(a) - 1) if a[i + 1] > a[i]]
    
    def valid(self, h, b, l, idx): 
        p = sorted(self.generate(h[:idx]))
        return b >= sum([p[i] for i in range(len(p) - l)])            
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        l = 0
        r = n - 1
        if self.valid(heights, bricks, ladders, n):
            return r
        while l <= r:
            m = (l + r) // 2
            if self.valid(heights, bricks, ladders, m):
                if not self.valid(heights, bricks, ladders, m + 1):
                    return m - 1
                l = m + 1
            else:
                r = m - 1
                
        
        
        
        