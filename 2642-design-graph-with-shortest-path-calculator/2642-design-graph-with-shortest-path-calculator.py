class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = {i: {} for i in range(n)}
        for s, d, c in edges:
            self.g[s][d] = c

    def addEdge(self, edge: List[int]) -> None:
        s, d, c = edge
        self.g[s][d] = c

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = float("inf")
        d = {i: INF for i in range(self.n)}
        d[node1] = 0
        h = [(0, node1)]
        while h:
            cd, cn = heappop(h)
            if cd > d[cn]:
                continue
            for neighbor, w in self.g[cn].items():
                dist = cd + w
                if dist < d[neighbor]:
                    d[neighbor] = dist
                    heappush(h, (dist, neighbor))
        return d[node2] if d[node2] != INF else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
