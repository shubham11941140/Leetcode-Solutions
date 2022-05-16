class Solution:

    def valid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m


    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
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
        
        # BFSVal v
        val = 0
        i = 0
        j = 0
        q = [(i, j, val)]
        v[i][j] = True
        while q:
            i, j, val = q.pop(0)
            # Check all 8 directions
            t = [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]
            for x, y in t:
                if self.valid(x, y, n, m) and grid[x][y] == 0 and not v[x][y]:
                    dp[x][y] = min(dp[x][y], val + 1)
                    v[x][y] = True
                    q.append((x, y, val + 1))
        
        if dp[n - 1][m - 1] in [-1, 10 ** 100]:
            return -1
        else:
            return dp[n - 1][m - 1] + 1
                    
        

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    val = 10 ** 100
                    if self.valid(i - 1, j, n, m) and grid[i - 1][j] == 0:
                        val = min(val, dp[i - 1][j])
                    if self.valid(i, j - 1, n, m) and grid[i][j - 1] == 0:
                        val = min(val, dp[i][j - 1])
                    if self.valid(i - 1, j - 1, n, m) and grid[i - 1][j - 1] == 0:
                        val = min(val, dp[i - 1][j - 1])
                    dp[i][j] = min(dp[i][j], val + 1)

        print(dp)
        print(dp[n - 1][m - 1])
        if dp[n - 1][m - 1] == -1:
            return -1
        else:
            return dp[n - 1][m - 1]