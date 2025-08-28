class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        diags = defaultdict(list)
        for i in range(n):
            for j in range(m):
                key = i - j
                heappush(diags[key], grid[i][j] if key < 0 else -grid[i][j])
        for i in range(n):
            for j in range(m):
                key = i - j
                grid[i][j] = heappop(diags[key]) if key < 0 else -heappop(diags[key])
        return grid        