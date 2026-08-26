class Solution:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        n, m = len(heightMap), len(heightMap[0])
        visited = [[False] * m for _ in range(n)]
        heap = []
        # Push all the boundary cells into the heap
        for i in range(n):
            for j in [0, m - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(m):
            for i in [0, n - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        water_trapped = 0
        while heap:
            height, x, y = heappop(heap)
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    water_trapped += max(0, height - heightMap[nx][ny])
                    heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        return water_trapped
