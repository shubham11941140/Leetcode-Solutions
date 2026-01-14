class Solution:

    @cache
    def dfs(self, i, j):
        self.v[i][j] = True
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                0 <= x < self.n
                and 0 <= y < self.m
                and not self.v[x][y]
                and self.g[x][y] == "1"
            ):
                self.dfs(x, y)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.g = grid
        self.n = len(grid)
        self.m = len(grid[0])
        c = 0
        self.v = [[False for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if self.g[i][j] == "1" and not self.v[i][j]:
                    self.dfs(i, j)
                    c += 1
        return c
