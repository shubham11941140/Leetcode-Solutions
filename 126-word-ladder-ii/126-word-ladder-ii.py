from random import choice

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
    
    def valid(self, a):
        n = len(a)
        for i in range(n - 1):
            if not self.distone(a[i], a[i + 1]):
                print(19, a[i], a[i + 1])
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
                #return adj
                #return level + 1            
            for i in range(k):
                if not visited[i]:                    
                    if self.distone(word, wordList[i]):
                        visited[i] = True
                        p = (wordList[i], level + 1)
                        q.append(p)
        #print(adj)  
                
        while [] in adj:
            adj.remove([])
            
        '''
        put = []
        for _ in range(1000):
            m = []
            for i in adj:
                m.append(choice(i))
            if m not in put:
                put.append(m)
        #return put
        # Check whether each is valid
        return [i for i in put if self.valid(i) and i[0] == beginWord and i[-1] == endWord]
        
        
        
        
        
        
        
        
        #print(adj) 
        put = []
        #print(adj[:10])
        for _ in range(10000):
            m = []
            for i in adj:
                m.append(choice(i))
            if m not in put:#print(m)
                put.append(m)
        #return put
        #print(put[:10])
        print(76)
        mv = []
        for j in put[:10]:
            print(j)
            if self.valid(j):
                print("IN")
                print(j)
        print([i for i in put if self.valid(i) and i[0] == beginWord and i[-1] == endWord])
        return [i for i in put if self.valid(i) and i[0] == beginWord and i[-1] == endWord]
        '''
        print(8)
        print(adj)
        idx = 1
        temp = [adj[0][0]]
        final = []
        self.prall(adj, idx, final, temp)
        print("FINAL STARTS")
        print(final)      

        #return []
        # Check whether each is valid
        #return put
        return [i for i in final if self.valid(i) and i[0] == beginWord and i[-1] == endWord]
        