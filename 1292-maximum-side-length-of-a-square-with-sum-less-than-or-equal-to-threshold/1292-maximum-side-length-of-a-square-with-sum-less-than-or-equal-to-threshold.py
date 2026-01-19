class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows, cols = len(mat), len(mat[0])

        p = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                p[r][c] = p[r-1][c] + p[r][c-1] - p[r-1][c-1] + mat[r-1][c-1]

        left, right, ans = 0, min(rows, cols), 0

        while left <= right:
            size = (left + right) // 2
            if self.exists(p, size, threshold, rows, cols):
                ans = size
                left = size + 1
            else:
                right = size - 1

        return ans

    def exists(self, p, size, limit, rows, cols):
        for r in range(size, rows + 1):
            for c in range(size, cols + 1):
                square_sum = p[r][c] - p[r-size][c] - p[r][c-size] + p[r-size][c-size]
                if square_sum <= limit:
                    return True
        return False        