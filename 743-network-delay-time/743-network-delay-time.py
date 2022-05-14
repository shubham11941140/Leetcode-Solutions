import heapq
from collections import defaultdict

class Solution:
    
    def dfs(self, k, adj, v):
        for i, e in adj[k]:
            if not v[i]:
                v[i] = True
                self.dfs(i, adj, v)  

    def calculate_distances(self, n, graph, starting_vertex):
        distances = {i:10**20 for i in range(n)}
        distances[starting_vertex] = 0

        pq = [(0, starting_vertex)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return max(distances.values())
    
    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Check all can be connected using a single DFS
        # If No return -1
        # If yes apply djikstra
        # DAG
        adj = [[] for i in range(n + 1)]
        #graph = [[0 for i in range(n)] for j in range(n)] 
        g = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])
            #graph[u - 1][v - 1] = w
            g[u - 1].append((v - 1, w))
        # Start at k
        v = [False for i in range(n + 1)]
        v[k] = True
        self.dfs(k, adj, v)
        print(v)
        if v.count(False) > 1:
            return -1
        # Call djikstra
        print(g)
        return self.calculate_distances(n, g, k - 1)
        

        
        