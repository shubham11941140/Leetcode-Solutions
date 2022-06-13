class Solution:
    
    def valid(self, i, n):
        return 0 <= i < n
    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # DP approach
        dp = [[10 ** 10 for j in i] for i in triangle]
        print(dp)
        n = len(triangle)
        for i in range(n):
            if i == 0:
                dp[i][0] = triangle[i][0]
            elif i > 0:
                c = len(dp[i - 1])
                for j in range(len(dp[i])):
                    for k in [j, j - 1]:
                        if self.valid(k, c):
                            dp[i][j] = min(dp[i][j], dp[i - 1][k] + triangle[i][j])
        print(dp)
        return min(dp[-1])
            
        