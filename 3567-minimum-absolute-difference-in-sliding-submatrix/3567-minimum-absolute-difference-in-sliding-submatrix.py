class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                v = sorted(set(
                    grid[x][y] for x in range(i, i + k) for y in range(j, j + k)
                ))
                lv = len(v)
                ans[i][j] = min(v[p+1] - v[p] for p in range(lv - 1)) if lv > 1 else 0
        return ans        