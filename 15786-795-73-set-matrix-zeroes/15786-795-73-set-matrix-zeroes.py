class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for x, y in [(i, j) for i in range(n) for j in range(m) if matrix[i][j] == 0]:
            for i in range(n):
                matrix[i][y] = 0
            for i in range(m):
                matrix[x][i] = 0        