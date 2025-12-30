class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def mg(i, j):
            s = set()
            for x in range(3):
                for y in range(3):
                    if grid[i + x][j + y] < 1 or grid[i + x][j + y] > 9:
                        return False
                    s.add(grid[i + x][j + y])
            if len(s) != 9:
                return False
            v1 = grid[i][j] + grid[i][j + 1] + grid[i][j + 2] == 15
            v2 = grid[i + 1][j] + grid[i + 1][j + 1] + grid[i + 1][j + 2] == 15
            v3 = grid[i + 2][j] + grid[i + 2][j + 1] + grid[i + 2][j + 2] == 15
            v4 = grid[i][j] + grid[i + 1][j] + grid[i + 2][j] == 15
            v5 = grid[i][j + 1] + grid[i + 1][j + 1] + grid[i + 2][j + 1] == 15
            v6 = grid[i][j + 2] + grid[i + 1][j + 2] + grid[i + 2][j + 2] == 15
            v7 = grid[i][j] + grid[i + 1][j + 1] + grid[i + 2][j + 2] == 15
            v8 = grid[i][j + 2] + grid[i + 1][j + 1] + grid[i + 2][j] == 15
            return (v1 and v2 and v3 and v4 and v5 and v6 and v7 and v8)
        return len([1 for i in range(len(grid) - 2) for j in range(len(grid[0]) - 2) if mg(i, j)])
