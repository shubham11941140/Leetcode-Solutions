class Solution:
    
    def cc(self, v, adj, idx):
        v[idx] = True
        for i in adj[idx]:
            if not v[i]:
                self.cc(v, adj, i)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        m = len(isConnected[0])
        adj = [[] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(m)
        v = [False for _ in range(n + 1)]
        return len([self.cc(v, adj, i) for i in range(n) if not v[i]])
        
