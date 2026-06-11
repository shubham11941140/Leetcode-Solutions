class Solution:

    def dfs(self, adj, node, par):
        a = [1 + self.dfs(adj, child, node) for child in adj[node] if child != par]
        return max(a) if a else 0

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return pow(2, self.dfs(adj, 1, -1) - 1, 10 ** 9 + 7)       