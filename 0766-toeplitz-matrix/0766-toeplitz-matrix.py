class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if i and j and matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True        