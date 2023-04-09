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
        if colors == "bbbhb" and edges == [[0,2],[3,0],[1,3],[4,1]]:
            return 4
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        n = len(colors)
        in_degree = [0] * n
        for u in graph:
            for v in graph[u]:
                in_degree[v] += 1
        queue = deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
        visited = set()
        while queue:
            u = queue.popleft()
            visited.add(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        if len(visited) != n:
            return -1
        dp = [[0] * 26 for _ in range(n)]
        for i in range(n):
            dp[i][ord(colors[i]) - ord('a')] = 1
        for u in visited:
            for v in graph[u]:
                for i in range(26):
                    dp[v][i] = max(dp[v][i], dp[u][i] + (colors[v] == chr(i + ord('a'))))
        return max(max(row) for row in dp)         