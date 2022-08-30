class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        a = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            for i in range(n):
                a[j][i] = matrix[n - 1 - i][j]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = a[i][j]
                
                
        