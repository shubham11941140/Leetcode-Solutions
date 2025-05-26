class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        q = deque([i for i in range(n) if not indegree[i]])
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i] + (i == ord(colors[v]) - ord('a')))
                indegree[v] -= 1
                if not indegree[v]:
                    q.append(v)
        return -1 if any(indegree) else max(max(dp[i]) for i in range(n))      