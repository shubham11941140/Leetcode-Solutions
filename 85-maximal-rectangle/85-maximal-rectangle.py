class Solution:

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i][j - 1] + 1 if j else 1
        r = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    w = dp[i][j]
                    for k in reversed(range(i + 1)):
                        w = min(w, dp[k][j])
                        r = max(r, w * (i - k + 1))
        return r
