class Solution:

    def minTime(self, n: int, edges: List[List[int]],
                hasApple: List[bool]) -> int:
        self.g = defaultdict(list)
        self.h = hasApple.copy()
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        return self.dfs(0, -1)

    def dfs(self, node, parent):
        time = 0
        for child in self.g[node]:
            if child != parent:
                time += self.dfs(child, node)
        if (time or self.h[node]) and parent != -1:
            time += 2
        return time
