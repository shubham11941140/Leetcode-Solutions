class Solution:
    
    def distone(self, a, b):
        n = len(a)
        c = 0
        for i in range(n):
            if a[i] != b[i]:
                c += 1
            if c > 1:
                return False            
        return True
    
    def prall(self, adj, idx, final, temp):
        if idx == len(adj):
            final.append(temp.copy())
            return
        for k in range(len(adj[idx])):
            if self.distone(temp[-1], adj[idx][k]):
                temp.append(adj[idx][k])
                self.prall(adj, idx + 1, final, temp)
                temp.pop()
            
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        k = len(wordList)
        if endWord not in wordList:
            return []
        q = []
        visited = [False] * k
        q.append((beginWord, 0))
        if k > 100:
            adj = [[] for i in range(100)]
        else:
            adj = [[] for i in range(k + 10)]
        while q:
            word, level = q.pop(0)
            adj[level].append(word)
            if level > 100:
                return []
            if word == endWord:
                ans = adj.copy()
                break           
            for i in range(k):
                if not visited[i]:                    
                    if self.distone(word, wordList[i]):
                        visited[i] = True
                        p = (wordList[i], level + 1)
                        q.append(p)                
        while [] in adj:
            adj.remove([])
        idx = 1
        temp = [adj[0][0]]
        final = []
        self.prall(adj, idx, final, temp)
        return [i for i in final if i[-1] == endWord]
        