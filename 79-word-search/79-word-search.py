class Solution:
    
    def valid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m    
    
    def recback(self, board, n, m, i, j, word, wordidx, visited):
        if wordidx == len(word):
            return True
        allvalid = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for x, y in allvalid:
            if self.valid(x, y, n, m) and not visited[x][y] and board[x][y] == word[wordidx]:
                visited[x][y] = True
                if self.recback(board, n, m, x, y, word, wordidx + 1, visited):
                    return True
                visited[x][y] = False
        return False
                            
    def exist(self, board: List[List[str]], word: str) -> bool:
        # REc back solution
        n = len(board)
        m = len(board[0])
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.recback(board, n, m, i, j, word, 1, visited):
                        return True
                    visited[i][j] = False
        return False
                
        