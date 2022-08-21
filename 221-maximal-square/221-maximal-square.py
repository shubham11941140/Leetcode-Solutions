class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1" and (i == 0 or j == 0):
                    dp[i][j] = 1
                elif matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                   dp[i - 1][j - 1]) + 1
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
        return max([max(i) for i in dp])**2
