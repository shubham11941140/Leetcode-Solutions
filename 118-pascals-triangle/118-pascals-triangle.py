class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[] for i in range(32)]
        a[0].append(1)
        for i in range(1, 32):
            b = a[i - 1].copy()
            for j in range(i):
                s = 0
                for k in [j - 1, j]:
                    if 0 <= k < len(b):
                        s += b[k]
                a[i].append(s)        
        a.pop(0)
        return a[:numRows]
                    
        