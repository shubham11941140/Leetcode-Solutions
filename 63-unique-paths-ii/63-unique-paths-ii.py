class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1 for i in range(n)] for j in range(m)]

        if obstacleGrid[0][0]:
            dp[0][0] = 0

        for j in range(1, n):
            dp[0][j] = dp[0][j - 1]
            if obstacleGrid[0][j]:
                dp[0][j] = 0

        for i in range(1, m):
            dp[i][0] = dp[i - 1][0]
            if obstacleGrid[i][0]:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if obstacleGrid[i][j]:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]
