class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        M = len(matrix)
        N = len(matrix[0])

        self.aux = [[0 for j in range(N)] for i in range(M)]

        for i in range(N):
            self.aux[0][i] = matrix[0][i]

        for i in range(1, M):
            for j in range(N):
                self.aux[i][j] = self.aux[i - 1][j] + matrix[i][j]

        for i in range(M):
            for j in range(1, N):
                self.aux[i][j] += self.aux[i][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        res = self.aux[row2][col2]

        if row1:
            res -= self.aux[row1 - 1][col2]

        if col1:
            res -= self.aux[row2][col1 - 1]

        if row1 and col1:
            res += self.aux[row1 - 1][col1 - 1]

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
