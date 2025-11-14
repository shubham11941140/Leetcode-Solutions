class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        return [
            [
                max(max(s) for s in [grid[x][j : j + 3] for x in range(i, i + 3)])
                for j in range(len(grid) - 2)
            ]
            for i in range(len(grid) - 2)
        ]
