class Solution:

    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = 0
        l = len([
            1 for i in grid for k in range(n)
            if i == [grid[j][k] for j in range(n)]
        ])
        return l
