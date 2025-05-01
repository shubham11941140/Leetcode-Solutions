class Solution:

    def minimumTime(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        heap = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0, 0))
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        while heap:
            time, r, c = heappop(heap)
            if r == ROWS - 1 and c == COLS - 1:
                return time
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    if grid[nr][nc] <= time + 1:
                        heappush(heap, [time + 1, nr, nc])
                    else:
                        heappush(
                            heap,
                            [
                                grid[nr][nc] + (0 if (grid[nr][nc] - time) % 2 else 1),
                                nr,
                                nc,
                            ],
                        )
        return -1
