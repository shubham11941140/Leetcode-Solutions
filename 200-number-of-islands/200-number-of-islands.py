class Solution:

    def dfs(self, grid, i, j, v, n, m):
        v[i][j] = True
        l = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
        for x, y in l:
            if 0 <= x < n and 0 <= y < m and not v[x][y] and grid[x][y] == "1":
                self.dfs(grid, x, y, v, n, m)
                
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        c = 0
        v = [[False for i in range(m)] for j in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not v[i][j]:
                    self.dfs(grid, i, j, v, n, m)
                    c += 1
        return c
                    
        