class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        a = [[0 for i in range(n)] for j in range(n)]
        for j in range(n):
            t = []
            for i in reversed(range(n)):
                t.append(matrix[i][j])
            print(t)
            for i in range(n):
                a[j][i] = t[i]
        print(a)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = a[i][j]
                
                
        