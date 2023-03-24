class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(-u)
        return self.dfs(graph, 0, set())

    def dfs(self, graph, node, visited):
        visited.add(node)
        count = 0
        for nei in graph[node]:
            if abs(nei) in visited:
                continue
            if nei > 0:
                count += 1
            count += self.dfs(graph, abs(nei), visited)
        return count
