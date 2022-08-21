class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        for minute in range(1000):
            q = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                            if 0 <= x < n and 0 <= y < m:
                                if grid[x][y] == 2:
                                    q.append((i, j))
                                    break
            if not q:
                for i in range(n):
                    for j in range(m):
                        if grid[i][j] == 1:
                            return -1                                
                return minute            
            for x, y in q:
                grid[x][y] = 2


                                
            
        
