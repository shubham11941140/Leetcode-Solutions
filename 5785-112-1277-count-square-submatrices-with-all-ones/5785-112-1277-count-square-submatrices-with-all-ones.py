class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        d = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]:
                    d[i][j] = (1 if 0 in [i, j] else
                               min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) +
                               1)
        return sum(sum(i) for i in d)
