class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque(
            [
                (i, j)
                for i in range(len(grid))
                for j in range(len(grid[0]))
                if grid[i][j] == 1
            ]
        )
        n = len(grid)
        m = len(grid[0])
        if len(queue) == 0 or len(queue) == len(grid) * len(grid[0]):
            return -1
        ans = 0
        while queue:
            ans += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    x = i + dx
                    y = j + dy
                    if 0 <= x < n and 0 <= y < m and not grid[x][y]:
                        grid[x][y] = 1
                        queue.append((x, y))
        return ans - 1
