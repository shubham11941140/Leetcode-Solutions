class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for v, u in roads:
            graph[v].add(u)
            graph[u].add(v)
        res = 0
        for v in graph:
            for u in graph:
                if u != v:
                    res = max(res, len(graph[v]) + len(graph[u]) - (v in graph[u]))
        return res        