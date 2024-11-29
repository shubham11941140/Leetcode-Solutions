class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        heap = [(grid[0][0], 0, 0)]
        visit = set()
        visit.add((0, 0))

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        while heap:
            time, r, c = heapq.heappop(heap)

            if r == ROWS - 1 and c == COLS - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visit:
                    visit.add((nr, nc))
                    if grid[nr][nc] <= time + 1:
                        heapq.heappush(heap, [time + 1, nr, nc])
                    else:
                        if (grid[nr][nc] - time) % 2 == 0:
                            heapq.heappush(heap, [grid[nr][nc] + 1, nr, nc])
                        else:
                            heapq.heappush(heap, [grid[nr][nc], nr, nc])
                        
        return -1        