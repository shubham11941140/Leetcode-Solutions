class Solution:

    def minCost(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, 2 * w))
        ans = [float("inf")] * n
        ans[0] = 0
        pq = [(0, 0)]
        while pq:
            weight, node = heapq.heappop(pq)
            if weight > ans[node]:
                continue
            for nd, wt in graph[node]:
                if wt + weight < ans[nd]:
                    ans[nd] = wt + weight
                    heapq.heappush(pq, (ans[nd], nd))
        return -1 if ans[n - 1] == float("inf") else ans[n - 1]
