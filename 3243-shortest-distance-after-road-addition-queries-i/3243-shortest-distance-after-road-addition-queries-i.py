class Solution:

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        # Initialize the adjacency list
        graph = [[] for _ in range(n)]

        # Add initial roads
        for i in range(n - 1):
            graph[i].append((i + 1, 1))

        def dijkstra():
            dist = [float("inf")] * n
            dist[0] = 0
            pq = [(0, 0)]  # (distance, node)

            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]:
                    continue
                for v, w in graph[u]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        heapq.heappush(pq, (dist[v], v))

            return dist[n - 1]

        result = []
        for u, v in queries:
            graph[u].append((v, 1))
            result.append(dijkstra())

        return result
