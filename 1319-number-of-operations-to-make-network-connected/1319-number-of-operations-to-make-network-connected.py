class Solution:
    def dfs(self, node):
        self.v[node] = True
        for i in self.a[node]:
            if not self.v[i]:
                self.dfs(i)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        self.a = [[] for i in range(n)]
        if len(connections) < n - 1:
            return -1
        for u, v in connections:
            self.a[u - 1].append(v - 1)
            self.a[v - 1].append(u - 1)
        ans = 0
        self.v = [False] * n
        for i in range(n):
            if not self.v[i]:                
                self.dfs(i)
                ans += 1
        return ans - 1
        