class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def isDisconnected(grid):
            def dfs(x, y):
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != 1:
                    return
                grid[x][y] = -1
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(x + dx, y + dy)
            
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        if count > 0:
                            return True
                        dfs(i, j)
                        count += 1
            return count != 1

        if isDisconnected([row[:] for row in grid]):
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if isDisconnected([row[:] for row in grid]):
                        return 1
                    grid[i][j] = 1

        return 2        