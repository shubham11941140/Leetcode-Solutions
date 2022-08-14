class Solution:
    
    def distone(self, a, b):
        return len([1 for i in range(self.wl) if a[i] != b[i]]) == 1
    
    def prall(self, idx, temp):
        t = temp[-1]
        if t == self.b:
            self.f.append(temp.copy()[::-1])
            return
        if idx == -1:
            return
        for i in self.a[idx]:
            if self.distone(t, i):
                #temp.append(i)
                self.prall(idx - 1, temp + [i])
                #temp.pop()
            
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        k = len(wordList)
        self.wl = len(beginWord)
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
                self.l = level
                break           
            for i in range(k):
                if not visited[i]:                    
                    if self.distone(word, wordList[i]):
                        visited[i] = True
                        p = (wordList[i], level + 1)
                        q.append(p)                
        while [] in adj:
            adj.remove([])
        self.a = adj.copy()
        #print(self.a)
        idx = len(self.a) - 2
        temp = [endWord]
        self.f = []
        self.b = beginWord
        self.prall(idx, temp)
        return self.f