class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        p += 0 if 0 <= x < n and 0 <= y < m and grid[x][y] else 1
        return p
