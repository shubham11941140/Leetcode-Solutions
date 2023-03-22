class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Create a graph
        graph = defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        # Find all connected components
        c = set()
        visited = set()
        q = deque([1])
        while q:
            u = q.popleft()
            if u not in visited:
                c.add(u)
                visited.add(u)
                for v, w in graph[u]:
                    q.append(v)
        # Find the minimum weight edge in the component
        m = []
        for u, v, w in roads:
            if u in c:
                m.append(w)
        return min(m)        