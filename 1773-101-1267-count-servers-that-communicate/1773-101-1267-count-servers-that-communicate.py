class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        row_count = [0] * rows
        col_count = [0] * cols
        # Count the number of servers in each row and column
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    row_count[r] += 1
                    col_count[c] += 1
        return len(
            [
                1
                for r in range(rows)
                for c in range(cols)
                if grid[r][c] == 1 and (row_count[r] > 1 or col_count[c] > 1)
            ]
        )
