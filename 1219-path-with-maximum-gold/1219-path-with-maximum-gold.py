class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            if not (0 <= x < len(grid) and 0 <= y < len(grid[0])
                    and grid[x][y] != 0):
                return 0
            gold = grid[x][y]
            grid[x][y] = 0  # mark as visited
            max_gold = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            grid[x][y] = gold  # backtrack
            return max_gold + gold

        m = [
            dfs(x, y) for x in range(len(grid)) for y in range(len(grid[0]))
            if grid[x][y]
        ]

        return max(m) if m else 0
