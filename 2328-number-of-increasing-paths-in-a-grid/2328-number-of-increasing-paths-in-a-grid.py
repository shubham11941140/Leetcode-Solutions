class Solution:        
    def countPaths(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        @lru_cache(None)
        def count(row, col):
            res = 1
            for dx, dy in [[row, col + 1], [row, col - 1], [row + 1, col], [row - 1, col]]:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] > grid[row][col]:
                    res += count(dx, dy) % (10 ** 9 + 7)
            return res
        return sum([count(i, j) for i in range(rows) for j in range(cols)]) % (10 ** 9 + 7)

      