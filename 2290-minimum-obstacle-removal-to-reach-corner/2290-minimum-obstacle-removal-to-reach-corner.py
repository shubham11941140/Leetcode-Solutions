class Solution:

    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pq = [(0, 0, 0)]  # (obstacles_removed, x, y)
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while pq:
            obstacles_removed, x, y = heappop(pq)
            if x == m - 1 and y == n - 1:
                return obstacles_removed
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heappush(pq, (obstacles_removed + grid[nx][ny], nx, ny))
        return -1
