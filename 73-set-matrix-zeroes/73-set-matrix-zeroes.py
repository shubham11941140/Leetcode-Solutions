class Solution:

    @staticmethod
    def setZeroes(matrix: List[List[int]]) -> None:
        """Do not return anything, modify matrix in-place instead."""
        a = []
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    a.append((i, j))
        for x, y in a:
            for i in range(n):
                matrix[i][y] = 0
            for i in range(m):
                matrix[x][i] = 0
        return m
