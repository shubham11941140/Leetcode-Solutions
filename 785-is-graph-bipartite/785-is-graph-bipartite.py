class Solution:

    def dfs(self, graph, visited, node):
        for i in graph[node]:
            if visited[i] == -1:
                visited[i] = 1 - visited[node]
                if not self.dfs(graph, visited, i):
                    return False
            elif visited[i] != -1 and visited[node] == visited[i]:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n
        for i in range(n):
            if visited[i] == -1:
                visited[i] = 1
                f = self.dfs(graph, visited, i)
                if not f:
                    return False
        return True
