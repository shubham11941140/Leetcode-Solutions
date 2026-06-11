class Solution:

    def dfs(self, adj, node, par):
        depth = 0

        for child in adj[node]:
            if child != par:
                depth = max(depth, 1 + self.dfs(adj, child, node))
        return depth

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = self.dfs(adj, 1, -1)

        res = pow(2, depth - 1, MOD)

        return res        