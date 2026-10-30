class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
        INF = 10 ** 18
        dist = [INF] * (n * k)
        dist[0] = 0
        heap = [(0, 0)]

        while heap:
            d, state = heappop(heap)
            if d > dist[state]:
                continue
            u, r = divmod(state, k)
            run = r + 1
            if u == n - 1:
                return d
            cu = labels[u]
            for v, w in adj[u]:
                nr = run + 1 if labels[v] == cu else 1
                if nr > k:
                    continue
                ns = v * k + nr - 1
                nd = d + w
                if nd < dist[ns]:
                    dist[ns] = nd
                    heappush(heap, (nd, ns))
        return -1