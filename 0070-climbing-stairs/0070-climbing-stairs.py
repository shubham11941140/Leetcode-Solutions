class Solution:
    
    def __init__(self):
        self.a = [1] * 2 + [0] * 45
        for i in range(2, 45 + 1):
            self.a[i] = self.a[i - 1] + self.a[i - 2]
    
    def climbStairs(self, n: int) -> int:
        return self.a[n]

        