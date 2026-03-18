class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0

        # Step 1: Column-wise prefix sum
        for i in range(1, m):
            for j in range(n):
                grid[i][j] += grid[i-1][j]

        # Step 2: Count valid subarrays per row
        for i in range(m):
            s = 0
            for j in range(n):
                s += grid[i][j]
                if s > k:
                    break
                ans += 1

        return ans        