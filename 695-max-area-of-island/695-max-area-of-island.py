class Solution:

    def dfs(self, i, j):
        self.v[i][j] = True
        self.val += 1
        for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
            if (0 <= x < self.n and 0 <= y < self.m and not self.v[x][y]
                    and self.g[x][y]):
                self.dfs(x, y)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.g = grid
        self.n = len(self.g)
        self.m = len(self.g[0])
        self.v = [[False for j in range(self.m)] for i in range(self.n)]
        self.a = 0
        for i in range(self.n):
            for j in range(self.m):
                if not self.v[i][j] and self.g[i][j]:
                    self.val = 0
                    self.dfs(i, j)
                    self.a = max(self.a, self.val)
        return self.a
