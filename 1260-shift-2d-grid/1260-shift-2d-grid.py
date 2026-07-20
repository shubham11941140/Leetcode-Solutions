class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        upd = [[0 for j in range(n)] for i in range(m)]
        for _ in range(k):
            for i in range(m):
                for j in range(n):
                    if i == m - 1 and j == n - 1:
                        upd[0][0] = grid[m - 1][n - 1]
                    elif j == n - 1:
                        upd[i + 1][0] = grid[i][n - 1]
                    else:
                        upd[i][j + 1] = grid[i][j]
            grid = upd.copy()
            upd = [[0 for j in range(n)] for i in range(m)]
        return grid
