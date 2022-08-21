class Solution:

    def nc(self, board, i, j, m, n):
        a = [(x, y) for x in [(i - 1), i, (i + 1)]
             for y in [(j - 1), j, (j + 1)]
             if (x, y) != (i, j) and 0 <= x < m and 0 <= y < n]
        return len([1 for x, y in a if board[x][y]])

    def gameOfLife(self, board: List[List[int]]) -> None:
        """Do not return anything, modify board in-place instead."""
        m = len(board)
        n = len(board[0])
        upd = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                lc = self.nc(board, i, j, m, n)
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
        for i in range(m):
            for j in range(n):
                board[i][j] = upd[i][j]
