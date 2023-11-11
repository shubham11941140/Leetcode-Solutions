class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.nodes = n
        self.graph = {i: {} for i in range(n)}

        # Populate the graph with edges and their costs
        for source, dest, cost in edges:
            self.graph[source][dest] = cost

    def addEdge(self, edge: List[int]) -> None:
        source, dest, cost = edge
        self.graph[source][dest] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = float("inf")

        # Initialize distances with infinity for all nodes
        distances = {node: INF for node in range(self.nodes)}
        distances[node1] = 0

        # Priority queue to store (distance, node) pairs
        heap = [(0, node1)]

        while heap:
            # Pop the node with the minimum distance from the heap
            curr_dist, curr_node = heapq.heappop(heap)

            # Skip if the current distance is greater than the known distance
            if curr_dist > distances[curr_node]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[curr_node].items():
                dist = curr_dist + weight

                # If a shorter path is found, update the distance and add to the heap
                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(heap, (dist, neighbor))

        # Return the shortest distance or -1 if no path exists
        return distances[node2] if distances[node2] != INF else -1


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
