class Solution:

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = []

        for i in range(n - 2):
            row = []
            for j in range(n - 2):
                max_val = max(
                    max(sub) for sub in [grid[x][j : j + 3] for x in range(i, i + 3)]
                )
                row.append(max_val)
            result.append(row)

        return result
