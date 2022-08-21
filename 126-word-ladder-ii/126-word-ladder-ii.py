class Solution:
    
    def distone(self, a, b):
        return [1 for i in range(self.wl) if a[i] != b[i]] == [1]
    
    def produce_all(self, idx, temp):
        t = temp[-1]
        if t == self.b:
            self.f.append(temp.copy())
            return
        if idx == -1:
            return
        for i in self.a[idx]:
            if self.distone(t, i):
                self.produce_all(idx - 1, temp + [i])
            
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        k = len(wordList)
        self.wl = len(beginWord)
        if endWord not in wordList:
            return []
        q = [(beginWord, 0)]
        visited = [False] * k
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
                break           
            for i in range(k):
                if not visited[i]:                    
                    if self.distone(word, wordList[i]):
                        visited[i] = True
                        q.append((wordList[i], level + 1))                
        while [] in adj:
            adj.remove([])
        self.a = adj.copy()
        idx = len(self.a) - 2
        temp = [endWord]
        self.f = []
        self.b = beginWord
        self.produce_all(idx, temp)
        return [i[::-1] for i in self.f]
