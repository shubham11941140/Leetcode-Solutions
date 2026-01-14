class Solution:

    def findTheCity(self, n: int, edges: List[List[int]],
                    distanceThreshold: int) -> int:
        ans = -1
        minCitiesCount = n
        dist = self.floydWarshall(n, edges, distanceThreshold)
        for i in range(n):
            cc = len([1 for j in range(n) if dist[i][j] <= distanceThreshold])
            if cc <= minCitiesCount:
                ans = i
                minCitiesCount = cc
        return ans

    def floydWarshall(self, n, edges, distanceThreshold):
        dist = [[distanceThreshold + 1] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
