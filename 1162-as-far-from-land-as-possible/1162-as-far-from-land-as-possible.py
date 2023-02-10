class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
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
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0:
                        grid[x][y] = 1
                        queue.append((x, y))
        return ans - 1
