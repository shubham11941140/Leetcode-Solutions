class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = 1  # Guard
        for r, c in walls:
            grid[r][c] = 1  # Wall
        # Mark cells guarded by the guards
        for r, c in guards:
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] == 1:  # Stop at a wall or another guard
                        break
                    if grid[nr][nc] == 0:  # Mark as guarded
                        grid[nr][nc] = 2
                    nr += dr
                    nc += dc
        return sum(1 for r in range(m) for c in range(n) if grid[r][c] == 0)