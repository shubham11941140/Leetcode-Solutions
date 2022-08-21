class Solution:
    
    def __init__(self):
        self.dp = [0] * 1000
        self.MOD = 10 ** 9 + 7
        self.dp[1] = 1        
        for i in range(2, 600):
            self.dp[i] = (self.dp[i - 1] * i * (2 * i - 1)) % self.MOD        
    
    def countOrders(self, n: int) -> int:
        return self.dp[n]
        
