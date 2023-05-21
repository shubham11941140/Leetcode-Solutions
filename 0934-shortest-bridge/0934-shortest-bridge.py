class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def dfs(v, c, i, j):
            v[i][j] = True
            grid[i][j] = c
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and not v[x][y] and grid[x][y]:
                    dfs(v, c, x, y)

        c = 2
        v = [[False for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if not v[i][j] and grid[i][j]:
                    dfs(v, c, i, j)
                    c += 1
        # print(grid)

        is1 = []
        is2 = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    is1.append((i, j))
                if grid[i][j] == 3:
                    is2.append((i, j))
        # print(is1, is2)

        m = []
        for x in is1:
            for y in is2:
                s = abs(x[0] - y[0]) + abs(x[1] - y[1])
                # print(s)
                m.append(s)
        # print(m)
        return min(m) - 1
        return 0
