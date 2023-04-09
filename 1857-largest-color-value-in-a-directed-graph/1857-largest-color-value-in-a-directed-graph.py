class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = collections.defaultdict(list)
        indegree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        q = collections.deque([i for i in range(n) if indegree[i] == 0])
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
        while q:
            u = q.popleft()
            for v in graph[u]:
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i] + (i == ord(colors[v]) - ord('a')))
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if any(indegree):
            return -1
        return max(max(dp[i]) for i in range(n))       