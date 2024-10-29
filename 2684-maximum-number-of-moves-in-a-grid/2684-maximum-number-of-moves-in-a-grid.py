class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])        
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            moves = 0
            for r, c in [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]:
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] > grid[row][col]:
                    moves = max(moves, 1 + dfs(r, c))
            memo[(row, col)] = moves
            return moves        
        memo = {}
        return max(dfs(row, 0) for row in range(rows))