class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.g = collections.defaultdict(list)
        self.l = labels
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        self.a = [0] * n
        self.dfs(0, None)
        return self.a

    def dfs(self, node, parent):
        c = Counter()
        for i in self.g[node]:
            if i != parent:
                c += self.dfs(i, node)
        c[self.l[node]] += 1
        self.a[node] = c[self.l[node]]
        return c       