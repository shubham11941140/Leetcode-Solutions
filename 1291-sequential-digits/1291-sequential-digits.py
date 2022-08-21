class Solution:
    
    def gen(self):
        a = list(range(1, 10))
        return [a[i:j] for i in range(9) for j in range(i, 10) if len(a[i:j]) > 1]
    
    def process(self, b):         
        return [int(i) for i in [''.join([str(k) for k in a]) for a in b]]                        
    
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        d = self.process(self.gen())
        return sorted([d[i] for i in range(len(d)) if low <= d[i] <= high])
                
