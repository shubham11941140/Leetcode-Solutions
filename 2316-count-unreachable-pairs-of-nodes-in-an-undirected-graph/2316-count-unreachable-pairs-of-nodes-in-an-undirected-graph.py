class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        self.g = defaultdict(list)
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        self.v = [False] * n
        comp = []
        for i in range(n):
            if not self.v[i]:
                c = []
                self.dfs(i, c)
                comp.append(c)
        l = [len(c) for c in comp]
        return sum([i * (n - i) for i in l]) // 2

    def dfs(self, node, component):
        self.v[node] = True
        component.append(node)
        for n in self.g[node]:
            if not self.v[n]:
                self.dfs(n, component)       