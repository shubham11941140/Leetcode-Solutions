class Solution:
    def bfs(self, node1, graph):
        queue = deque()
        queue.append((node1, 0))
        visited = set()
        visited.add(node1)
        a = defaultdict(int)
        while queue:
            node, dist = queue.popleft()
            #if dist:
            a[node] = dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return a

    def process(self, a, b):
        v = set()
        for i in a:
            if i in b:
                m = max(a[i], b[i])
                v.add(m)
        if not v:
            return -1
        mv = min(v)
        ans = []
        for i in a:
            if i in b:
                m = max(a[i], b[i])
                if m == mv:
                    ans.append(i)
        return min(ans)

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        n = len(edges)
        for i in range(n):
            if edges[i] != -1:
                graph[i].append(edges[i])
        a = self.bfs(node1, graph)
        b = self.bfs(node2, graph)
        print(a, b)
        return self.process(a, b)