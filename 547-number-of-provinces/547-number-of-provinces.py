class Solution:
    
    def cc(self, v, adj, idx):
        v[idx] = True
        for i in adj[idx]:
            if not v[i]:
                self.cc(v, adj, i)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # no of dfs calls
        # Make the adj list
        n = len(isConnected)
        m = len(isConnected[0])
        adj = [[] for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
                    adj[j].append(m)
        print(adj)
        v = [False for _ in range(n + 1)]
        p = 0
        for i in range(n):
            if not v[i]:
                self.cc(v, adj, i)
                p += 1
        return p
        