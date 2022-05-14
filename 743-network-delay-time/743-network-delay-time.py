import heapq

class Solution:
    
    def dfs(self, k, adj, v):
        for i, e in adj[k]:
            if not v[i]:
                v[i] = True
                self.dfs(i, adj, v)
                
    def printSolution(self, n, dist):
        print("Vertex \tDistance from Source")
        for node in range(n):
            print(node, "\t", dist[node])                
                
    def minDistance(self, n, dist, sptSet):
        m = 10 ** 20
        min_index = -1
        for u in range(n):
            if dist[u] < m and sptSet[u] == False:
                m = dist[u]
                min_index = u
        print(21, min_index)
        return min_index
    
    def dijkstra(self, graph, n, src):
        dist = [10 ** 20] * n
        dist[src] = 0
        sptSet = [False] * n
        for cout in range(n):
            x = self.minDistance(n, dist, sptSet)
            sptSet[x] = True
            for y in range(n):
                if graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + graph[x][y]:
                    dist[y] = dist[x] + graph[x][y]
        self.printSolution(n, dist)
        return max(dist)
    
    def topologicalSortUtil(self,g,v,visited,stack):
        print(38, v)
        visited[v] = True
        if v in g.keys():
            for node,weight in g[v]:
                if visited[node] == False:
                    self.topologicalSortUtil(g,node,visited,stack)
        stack.append(v)
        
    def shortestPath(self, g, n, s):
        visited = [False]*n
        stack =[]
        self.topologicalSortUtil(g, s,visited,stack)
        dist = [float("Inf")] * n
        dist[s] = 0
        while stack:
            i = stack.pop()
            for node,weight in g[i]:
                if dist[node] > dist[i] + weight:
                    dist[node] = dist[i] + weight
        for i in range(n):            
            print (("%d" %dist[i]) if dist[i] != float("Inf") else "Inf" ,end=" ")
        return max([i for i in dist if i != float("inf")])

    



    def calculate_distances(self, graph, starting_vertex):
        distances = {vertex: float('infinity') for vertex in graph}
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

        return distances    
    
    
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Check all can be connected using a single DFS
        # If No return -1
        # If yes apply djikstra
        # DAG
        adj = [[] for i in range(n + 1)]
        graph = [[0 for i in range(n)] for j in range(n)] 
        g = defaultdict(list)
        for u, v, w in times:
            adj[u].append([v, w])
            graph[u - 1][v - 1] = w
            g[u - 1].append((v - 1, w))
        # Start at k
        v = [False for i in range(n + 1)]
        v[k] = True
        self.dfs(k, adj, v)
        print(v)
        if v.count(False) > 1:
            return -1
        # Call djikstra
        f = self.dijkstra(graph, n, k - 1)
        b = self.shortestPath(g, n, k - 1)
        h = self.calculate_distances(g, k - 1)
        print()
        print(f, b)
        print(112, h)
        m = max(h.values())
        return min(f, b, m)
        

        
        