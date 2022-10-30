class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0
        q = deque([(0, 0, 0, 0)])
        visited = set((0, 0, 0))
        while q:
            x, y, z, dist = q.popleft()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if not grid[nx][ny]:
                        if (nx, ny, z) not in visited:
                            if nx == n - 1 and ny == m - 1:
                                return dist + 1
                            visited.add((nx, ny, z))
                            q.append((nx, ny, z, dist + 1))
                    else:
                        if z + 1 > k:
                            continue
                        if (nx, ny, z + 1) not in visited:
                            if nx == n - 1 and ny == m - 1:
                                return dist + 1
                            visited.add((nx, ny, z + 1))
                            q.append((nx, ny, z + 1, dist + 1))
        return -1      