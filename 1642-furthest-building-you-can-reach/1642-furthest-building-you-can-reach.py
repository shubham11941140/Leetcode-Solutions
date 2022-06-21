class Solution:
    
    
    def generate(self, a):
        n = len(a)
        b = []
        for i in range(n - 1):
            if a[i + 1] > a[i]:
                v = a[i + 1] - a[i]
                b.append(v)
        return b
    
    def valid(self, h, b, l, idx): 
        #print("IDX", idx, h[:idx])
        p = self.generate(h[:idx])
        #print(p)
        p.sort()
        #print(p)
        t = len(p) - l
        print(t)
        s = 0
        for i in range(t):
            s += p[i]
        print(s, b)
        return b >= s
        
    
    
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # Greedy
        # Make array
        n = len(heights)
        a = []
        for i in range(n - 1):
            if heights[i + 1] > heights[i]:
                diff = heights[i + 1] - heights[i]
                f = [diff, i, i + 1]
                a.append(f)
        #print(a)
        # BS to move on the indices
        l = 0
        r = n - 1
        if self.valid(heights, bricks, ladders, n):
            print("BOOM", r, n)
            return n - 1
        c = 0
        while l <= r:
            c += 1
            if c > 100:
                break
            m = (l + r) // 2
            print(l, m, r)
            if self.valid(heights, bricks, ladders, m):
                print("M IS ", m)
                print("FOR M+1", self.valid(heights, bricks, ladders, m + 1))
                if not self.valid(heights, bricks, ladders, m + 1):
                    return m - 1
                print("Valid Index", m)
                l = m + 1
            else:
                r = m - 1
                
        
        
        
        