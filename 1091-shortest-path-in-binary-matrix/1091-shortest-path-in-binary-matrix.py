class Solution:

    @staticmethod
    def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])                                
        dp = [[-1 for j in range(m)] for i in range(n)]
        v = [[False for j in range(m)] for i in range(n)]  
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dp[i][j] = 10 ** 100
        dp[0][0] = 0        
        if grid[0][0] == 1:
            return -1
        q = [(0, 0, 0)]
        v[0][0] = True
        while q:
            i, j, val = q.pop(0)
            if i == n - 1 and j == m - 1:
                if dp[n - 1][m - 1] not in [-1, 10 ** 100]:
                    return dp[n - 1][m - 1] + 1
                return -1
            for x, y in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == 0 and not v[x][y]:
                    dp[x][y] = min(dp[x][y], val + 1)
                    v[x][y] = True
                    q.append((x, y, val + 1))        
        return -1
