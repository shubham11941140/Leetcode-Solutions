class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n, dir = len(grid), len(grid[0]), [-1,0,1,0,-1]        
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or not grid[i][j]:
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            return res + sum([dfs(i + dir[k], j + dir[k + 1]) for k in range(4)])
        v = [dfs(i, j) for i in range(m) for j in range(n) if grid[i][j]]
        return max(v) if v else 0   