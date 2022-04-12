class Solution:
    
    
    def valid(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n
    
    def nc(self, board, i, j, m, n):
        a = []
        for x in [(i - 1), i, (i + 1)]:
            for y in [(j - 1), j, (j + 1)]:
                if (x, y) != (i, j) and self.valid(x, y, m, n):
                    a.append((x, y))
        lc = 0
        dc = 0
        for x, y in a:
            if board[x][y]:
                lc += 1
            else:
                dc += 1
        return lc, dc                                        
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        upd = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                lc, dc = self.nc(board, i, j, m, n)
                if board[i][j]:
                    if lc < 2:
                        upd[i][j] = 0
                    elif lc in [2, 3]:
                        upd[i][j] = 1
                    elif lc > 3:
                        upd[i][j] = 0
                else:
                    if lc == 3:
                        upd[i][j] = 1
        print(upd)
        for i in range(m):
            for j in range(n):
                board[i][j] = upd[i][j]
                
            
        