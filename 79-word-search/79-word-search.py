class Solution:

    def recback(self, board, n, m, i, j, word, wordidx, visited, lw):
        if wordidx == lw:
            return True
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if (0 <= x < n and 0 <= y < m and not visited[x][y]
                    and board[x][y] == word[wordidx]):
                visited[x][y] = True
                if self.recback(board, n, m, x, y, word, wordidx + 1, visited,
                                lw):
                    return True
                visited[x][y] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        # REc back solution
        n = len(board)
        m = len(board[0])
        lw = len(word)
        visited = [[False for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if self.recback(board, n, m, i, j, word, 1, visited, lw):
                        return True
                    visited[i][j] = False
        return False
