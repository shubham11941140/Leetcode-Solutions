class Solution:  

    def cherryPickup(self, grid: List[List[int]]) -> int:

        @cache
        def rec(i, j1, j2):

            if j1 > j2: 
                return rec(i, j2, j1) 

            if i == len(grid) or j1 == -1 or j2 == len(grid[0]): 
                return 0 

            b = max(rec(i + 1, j1 + d1, j2 + d2) for d1 in range(-1, 2) for d2 in range(-1, 2))

            return b + (grid[i][j1] + grid[i][j2] if j1 != j2 else grid[i][j1]) 

        return rec(0, 0, len(grid[0]) - 1)
