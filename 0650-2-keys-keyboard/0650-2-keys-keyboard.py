class Solution:
    
    def __init__(self):
        self.d = [1000 for i in range(1015)]
        self.d[1] = 0
        for i in range(2, 1010):
            for j in range(2, i + 1):
                if i == j:
                    self.d[i] = min(self.d[i], i)
                if i % j == 0:
                    self.d[i] = min(self.d[i], self.d[j] + (i // j))        
        
    def minSteps(self, n: int) -> int:        
        return self.d[n]                    
        