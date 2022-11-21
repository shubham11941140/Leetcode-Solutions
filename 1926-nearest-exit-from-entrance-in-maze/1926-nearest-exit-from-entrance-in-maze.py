class Solution:

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n, m = len(maze), len(maze[0])
        q = collections.deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        while q:
            x, y, d = q.popleft()
            if (x == 0 or x == n - 1 or y == 0 or y == m - 1) and (x, y) != (
                    entrance[0],
                    entrance[1],
            ):
                return d
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == ".":
                    maze[nx][ny] = "+"
                    q.append((nx, ny, d + 1))
        return -1
