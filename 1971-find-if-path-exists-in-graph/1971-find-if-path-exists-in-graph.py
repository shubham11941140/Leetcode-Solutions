class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()
        queue = deque([source])
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    queue.append(nei)
        return False        