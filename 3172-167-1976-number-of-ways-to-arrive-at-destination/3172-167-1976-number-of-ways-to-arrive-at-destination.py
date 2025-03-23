class Solution:

    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        adj = defaultdict(list)
        for u, v, t in roads:
            adj[u].append((v, t))
            adj[v].append((u, t))
        shortesttime = [10**20] * n
        cnt = [0] * n
        pq = [(0, 0)]  # (time, node)

        shortesttime[0] = 0
        cnt[0] = 1

        while pq:
            time, node = heappop(pq)
            if time > shortesttime[node]:
                continue
            for nbr, rtime in adj[node]:
                if time + rtime < shortesttime[nbr]:
                    shortesttime[nbr] = time + rtime
                    cnt[nbr] = cnt[node]
                    heappush(pq, (shortesttime[nbr], nbr))
                elif time + rtime == shortesttime[nbr]:
                    cnt[nbr] = (cnt[nbr] + cnt[node]) % mod
        return cnt[-1]
