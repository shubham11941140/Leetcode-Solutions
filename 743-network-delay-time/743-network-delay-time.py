from heapq import *
from collections import defaultdict

class Solution:

    def calculate_distances(self, n, graph, starting_vertex):
        distances = {i: 10 ** 20 for i in range(n)}
        distances[starting_vertex] = 0
        pq = [(0, starting_vertex)]
        while pq:
            current_distance, current_vertex = heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heappush(pq, (distance, neighbor))
        m = max(distances.values())
        return -1 if m == 10 ** 20 else m                    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = defaultdict(list)
        for u, v, w in times:
            g[u - 1].append((v - 1, w))
        return self.calculate_distances(n, g, k - 1)
        

        
        