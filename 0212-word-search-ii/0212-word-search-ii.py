class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []

        def Trie():
            return defaultdict(Trie)

        root = Trie()

        def add(s):
            cur = root
            for c in s:
                cur = cur[c]
            cur["$"] = s

        for word in words:
            add(word)
        m, n = len(board), len(board[0])

        def dfs(i, j, root):
            ch = board[i][j]
            cur = root.get(ch)
            if not cur:
                return

            if "$" in cur:
                res.append(cur["$"])
                del cur["$"]

            board[i][j] = "#"
            if i < m - 1:
                dfs(i + 1, j, cur)
            if i > 0:
                dfs(i - 1, j, cur)
            if j < n - 1:
                dfs(i, j + 1, cur)
            if j > 0:
                dfs(i, j - 1, cur)
            board[i][j] = ch

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)
        return res
