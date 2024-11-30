class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        graph = {i: [[], []] for i in range(n)}
        for u, v in redEdges:
            graph[u][0].append(v)
        for u, v in blueEdges:
            graph[u][1].append(v)
        res = [float("inf")] * n
        res[0] = 0
        q = deque([(0, 0, 0), (0, 1, 0)])
        visited = set([(0, 0), (0, 1)])
        while q:
            node, color, dist = q.popleft()
            for nei in graph[node][color]:
                if (nei, 1 - color) not in visited:
                    res[nei] = min(res[nei], dist + 1)
                    q.append((nei, 1 - color, dist + 1))
                    visited.add((nei, 1 - color))
        return [x if x != float("inf") else -1 for x in res]
