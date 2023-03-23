class Solution:
    def dfs(self, visited, adj, node):
        visited[node] = True
        for i in adj[node]:
            if not visited[i]:
                self.dfs(visited, adj, i)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj = [[] for i in range(n)]
        if len(connections) < n - 1:
            return -1
        for u, v in connections:
            adj[u - 1].append(v - 1)
            adj[v - 1].append(u - 1)
        ans = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:                
                self.dfs(visited, adj, i)
                ans += 1
        return ans - 1
        