class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        down = [1] + [0] * (len(grid[0]) - 1)
        for row in grid:
            right = 0
            for j, mirror in enumerate(row):
                if mirror:
                    right, down[j] = down[j], right
                else:
                    right = down[j] = right + down[j]
        return down[-1] % (10 ** 9 + 7)