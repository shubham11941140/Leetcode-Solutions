class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        Trie = lambda : defaultdict(Trie)
        root = Trie()
                
        for word in words: 
            cur = root
            for c in word: 
                cur = cur[c]
            cur['$'] = word
            
        m, n = len(board), len(board[0])
        
        def dfs(i, j, root):
            ch = board[i][j]
            cur = root.get(ch)
            if not cur: 
                return 

            if '$' in cur: 
                res.append(cur['$'])
                del cur['$']
            
            board[i][j] = '#'
            if i < m - 1: 
                dfs(i + 1, j, cur)
            if i: 
                dfs(i - 1, j, cur)
            if j < n - 1: 
                dfs(i, j + 1, cur)
            if j: 
                dfs(i, j - 1, cur)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res