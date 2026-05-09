class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        layers = min(m, n) // 2

        for layer in range(layers):

            top = layer
            bottom = m - layer - 1
            left = layer
            right = n - layer - 1

            arr = [grid[top][j] for j in range(left, right + 1)] + \
                    [grid[i][right] for i in range(top + 1, bottom)] + \
                    [grid[bottom][j] for j in range(right, left - 1, -1)] + \
                    [grid[i][left] for i in range(bottom - 1, top, -1)]

            rot = k % len(arr)
            rotated = arr[rot:] + arr[:rot]
            idx = 0

            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            for i in range(top + 1, bottom):
                grid[i][right] = rotated[idx]
                idx += 1

            for j in range(right, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid        