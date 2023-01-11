class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return self.dfs(graph, hasApple, 0, -1)

    def dfs(self, graph, hasApple, node, parent):
        time = 0
        for child in graph[node]:
            if child != parent:
                time += self.dfs(graph, hasApple, child, node)
        if (time > 0 or hasApple[node]) and parent != -1:
            time += 2
        return time        