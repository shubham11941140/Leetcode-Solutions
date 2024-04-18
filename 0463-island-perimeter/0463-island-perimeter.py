class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    a = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    for x, y in a:
                        if 0 <= x < n and 0 <= y < m:
                            if grid[x][y]:
                                p += 0
                            else:
                                p += 1
                        else:
                            p += 1
        print(p)
        return p
                    
        