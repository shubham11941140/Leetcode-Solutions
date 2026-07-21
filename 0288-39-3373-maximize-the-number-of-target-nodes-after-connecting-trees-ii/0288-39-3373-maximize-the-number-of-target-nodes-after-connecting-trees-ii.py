class Solution:

    def buildList(self, edges):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return adj

    def dfsColor(self, adj, u, parent, color, isA):
        if color[u] == 0:
            if isA:
                self.evenA += 1
            else:
                self.evenB += 1
        else:
            if isA:
                self.oddA += 1
            else:
                self.oddB += 1

        for v in adj[u]:
            if v != parent:
                color[v] = color[u] ^ 1
                self.dfsColor(adj, v, u, color, isA)

    def maxTargetNodes(self, edges1: List[List[int]],
                       edges2: List[List[int]]) -> List[int]:
        adjA = self.buildList(edges1)
        adjB = self.buildList(edges2)
        n, m = len(adjA), len(adjB)
        colorA = [0] + [-1] * (n - 1)
        colorB = [0] + [-1] * (m - 1)
        self.evenA = self.oddA = self.evenB = self.oddB = 0
        self.dfsColor(adjA, 0, -1, colorA, True)
        self.dfsColor(adjB, 0, -1, colorB, False)
        maxiB = max(self.evenB, self.oddB)
        return [(self.evenA if colorA[i] == 0 else self.oddA) + maxiB
                for i in range(n)]
