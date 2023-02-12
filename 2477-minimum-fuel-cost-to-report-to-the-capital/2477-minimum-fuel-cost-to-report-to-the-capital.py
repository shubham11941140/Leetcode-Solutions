class Solution:
    def dfs(self, v, par):
        t = 1
        for i in self.g[v]:
            if i != par:
                p, c = self.dfs(i, v)
                t += p
                self.r += c
        return t, ceil(t / self.s)

    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        self.g = defaultdict(list)
        self.s = seats
        self.r = 0
        for u, v in roads:
            self.g[u].append(v)
            self.g[v].append(u)
        self.dfs(0, None)
        return self.r