class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)
        for idx, (i, j) in enumerate(edges):
            graph[i].append((j, succProb[idx]))
            graph[j].append((i, succProb[idx]))
        stack = [(-1, start)]
        visit = set([start])
        probability = [0] * n
        while stack:
            prob, a = heapq.heappop(stack)
            if probability[a] != 0:
                continue
            probability[a] = prob
            for v, p in graph[a]:
                if probability[v] == 0:
                    visit.add(v)
                    heapq.heappush(stack, (prob * p, v))
        return -probability[end]
