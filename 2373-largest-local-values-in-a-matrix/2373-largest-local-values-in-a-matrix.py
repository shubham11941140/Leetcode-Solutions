class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                row.append(
                    max(max(s) for s in [grid[x][j : j + 3] for x in range(i, i + 3)])
                )
            result.append(row)

        return result
