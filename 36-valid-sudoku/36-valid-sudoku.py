class Solution:
    
    def check(self, a):
        while "." in a:
            a.remove(".")
        a = [int(i) for i in a]
        if not a:
            return True
        return len(set(a)) == len(a) and min(a) >= 1 and max(a) <= 9
    
    def rows(self, board):
        return len([1 for i in board if self.check(i)]) == 9
    
    def generatecolumns(self, board):
        return [[i[j] for i in board] for j in range(9)]
    
    def grid(self, board, i, j):
        return [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
    
    def all_grid(self, board, idx):
        return [self.grid(board, i, j) for i in idx for j in idx]
                            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        c = self.generatecolumns(board)
        g = self.all_grid(board, [0, 3, 6])
        return self.rows(board) and self.rows(c) and self.rows(g)
    