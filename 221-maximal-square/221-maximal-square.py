class Solution:
    
    def check(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m
    
    def fullone(self, i, j, c, matrix):
        ans = -1
        for c_var in reversed(range(1, c + 1)):
            b = 0
            for x in range(i, i + c_var):
                for y in range(j, j + c_var):
                    #if i == 0 and j == 0:                        print("XY", x, y)
                    try:
                        if matrix[x][y] == "1":
                            b += 1
                    except:
                        pass
            #if c_var == 4:                print("B at 4", b)
            if b == (c_var * c_var):
                return c_var
                ans = max(ans, c_var)
        #print("FANS", ans)
        return -1
                        
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in matrix:
            print(*i)
        n = len(matrix)
        m = len(matrix[0])
        print(n, m, True)
        dp = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == "1" and (i == 0 or j == 0):
                    dp[i][j] = 1
                elif matrix[i][j] == "1":
                    v = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                    dp[i][j] = v + 1
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
        for i in dp:
            print(*i)
        f = max([max(i) for i in dp])
        return f ** 2
        print(45)
        
        
        #return n
        ans = -1
        for i in range(n):
            for j in range(m):
                c = 0
                if matrix[i][j] == "1":
                    x = i
                    y = j
                    #print(x, y)
                    while self.check(x, y, n, m) and matrix[x][y] == "1":
                        c += 1
                        x += 1
                        y += 1
                    #print("C", c)
                    flag = self.fullone(i, j, c, matrix)
                    if flag != -1:
                        ans = max(ans, flag)
        #print("ANS", ans)
        if ans == -1:
            return 0
        return ans ** 2
                    
                    
        
        