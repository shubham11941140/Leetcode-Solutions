class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        count = [1] * n
        dist = [0] * n
        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    dist[node] += dist[child] + count[child]
        dfs(0, None)
        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    dist[child] = dist[node] - count[child] + n - count[child]
                    dfs2(child, node)
        dfs2(0, None)
        return dist        