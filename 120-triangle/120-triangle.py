class Solution:    
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[10 ** 10 for j in i] for i in triangle]
        dp[0][0] = triangle[0][0]
        n = len(triangle)
        for i in range(1, n):
            c = len(dp[i - 1])
            for j in range(len(dp[i])):
                for k in [j, j - 1]:
                    if 0 <= k < c:
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + triangle[i][j])
        return min(dp[-1])
            
        