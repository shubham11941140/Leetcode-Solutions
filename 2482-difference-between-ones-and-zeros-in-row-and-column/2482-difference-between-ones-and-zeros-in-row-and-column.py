class Solution:

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        rows = [0] * m
        cols = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        diff = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rows[i] + cols[j] - (n - rows[i]) - (m - cols[j])
        return diff
