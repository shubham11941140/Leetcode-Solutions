class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        A = grid.copy()

        def dfs(i, j):
            if i < 0 or j < 0 or i == len(A) or j == len(A[0]):
                return
            if A[i][j] == 0:
                return
            A[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(A)):
            dfs(i, 0)
            dfs(i, len(A[0]) - 1)

        for j in range(len(A[0])):
            dfs(0, j)
            dfs(len(A) - 1, j)

        return sum(sum(row) for row in A)
