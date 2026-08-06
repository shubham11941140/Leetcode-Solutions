class Solution:

    def dfs(self, v, i, j, val):
        if i < 0 or j < 0 or i >= self.n or j >= self.m:
            return
        if self.h[i][j] < val or v[i][j]:
            return
        v[i][j] = True
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            self.dfs(v, x, y, self.h[i][j])

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.n = len(heights)
        self.m = len(heights[0])
        self.h = heights
        a = [[False for i in range(self.m)] for j in range(self.n)]
        p = [[False for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if i == 0 or j == 0:
                    self.dfs(a, i, j, 0)
                if i == self.n - 1 or j == self.m - 1:
                    self.dfs(p, i, j, 0)
        return [[i, j] for i in range(self.n) for j in range(self.m)
                if a[i][j] and p[i][j]]
