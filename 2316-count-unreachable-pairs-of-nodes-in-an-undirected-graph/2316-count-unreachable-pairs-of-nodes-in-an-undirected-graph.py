class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        # Find the connected components
        visited = set()
        components = []
        for node in range(n):
            if node not in visited:
                component = []
                self.dfs(node, graph, visited, component)
                components.append(component)
        # print(components)
        l = [len(component) for component in components]
        c = 0
        for i in range(len(l)):
            c += l[i] * (n - l[i])
        return c // 2

    def dfs(self, node, graph, visited, component):
        visited.add(node)
        component.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                self.dfs(neighbor, graph, visited, component)
