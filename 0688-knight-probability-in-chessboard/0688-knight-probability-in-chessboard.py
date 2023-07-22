class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Possible moves of a knight
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        def is_valid(x, y):
            return 0 <= x < n and 0 <= y < n

        memo = {}

        def dp(k, x, y):
            if not (0 <= x < n and 0 <= y < n):
                return 0
            if k == 0:
                return 1

            if (k, x, y) in memo:
                return memo[(k, x, y)]

            total_prob = 0
            for dx, dy in moves:
                total_prob += dp(k - 1, x + dx, y + dy)

            memo[(k, x, y)] = total_prob / 8
            return memo[(k, x, y)]

        return dp(k, row, column)        