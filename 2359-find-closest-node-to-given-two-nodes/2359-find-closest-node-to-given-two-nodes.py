class Solution:
    def bfs(self, node1):
        queue = deque()
        queue.append((node1, 0))
        visited = set()
        visited.add(node1)
        a = defaultdict(int)
        while queue:
            node, dist = queue.popleft()
            a[node] = dist
            for neighbor in self.g[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return a

    def process(self, a, b):
        v = [max(a[i], b[i]) for i in a if i in b]
        if not v:
            return -1
        mv = min(v)
        return min([i for i in a if i in b and max(a[i], b[i]) == mv])

    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        self.g = defaultdict(list)
        n = len(edges)
        for i in range(n):
            if edges[i] != -1:
                self.g[i].append(edges[i])
        a = self.bfs(node1)
        b = self.bfs(node2)
        return self.process(a, b)