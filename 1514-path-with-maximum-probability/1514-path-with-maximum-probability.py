class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g = defaultdict(list)
        for idx, (i, j) in enumerate(edges):
            g[i].append((j, succProb[idx]))
            g[j].append((i, succProb[idx]))
        s = [(-1, start)]
        vi = set([start])
        pr = [0] * n
        while s:
            prob, a = heappop(s)
            if pr[a]:
                continue
            pr[a] = prob
            for v, p in g[a]:
                if pr[v] == 0:
                    vi.add(v)
                    heappush(s, (prob * p, v))
        return - pr[end]        