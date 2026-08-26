class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]],
                       k: int) -> List[int]:

        def buildGraph(edges):
            graph = {i: [] for i in range(len(edges) + 1)}
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        def dfs(g, node, prev, d):
            return 1 + (0 if d == 0 else sum(
                [dfs(g, nei, node, d - 1) for nei in g[node] if nei != prev]))

        graph1 = buildGraph(edges1)
        graph2 = buildGraph(edges2)
        m2 = (max([dfs(graph2, i, -1, k - 1)
                   for i in range(len(edges2) + 1)]) if k else 0)
        return [m2 + dfs(graph1, i, -1, k) for i in range(len(edges1) + 1)]
