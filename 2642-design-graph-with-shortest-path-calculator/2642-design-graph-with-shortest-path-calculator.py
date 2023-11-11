class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.g = {i: {} for i in range(n)}
        for source, dest, cost in edges:
            self.g[source][dest] = cost

    def addEdge(self, edge: List[int]) -> None:
        source, dest, cost = edge
        self.g[source][dest] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = float("inf")
        distances = {node: INF for node in range(self.n)}
        distances[node1] = 0
        heap = [(0, node1)]

        while heap:
            curr_dist, curr_node = heapq.heappop(heap)
            if curr_dist > distances[curr_node]:
                continue
            for neighbor, weight in self.g[curr_node].items():
                dist = curr_dist + weight
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (dist, neighbor))
        return distances[node2] if distances[node2] != INF else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
