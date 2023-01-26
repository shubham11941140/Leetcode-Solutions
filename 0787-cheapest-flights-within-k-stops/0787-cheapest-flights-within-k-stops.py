class Solution:

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                          dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        q = [(0, src, k + 1)]
        vis = [10**10] * n
        vis[src] = 0
        while q:
            price, node, stops = q.pop(0)
            if stops:
                for v, w in graph[node]:
                    alt = price + w
                    if alt <= vis[v]:
                        q.append((alt, v, stops - 1))
                        vis[v] = alt
        return -1 if vis[dst] == 10**10 else vis[dst]
