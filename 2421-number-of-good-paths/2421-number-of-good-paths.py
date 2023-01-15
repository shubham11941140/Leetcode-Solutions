class Solution:
    def get_root(self, i):
        return i if i == self.par[i] else self.get_root(self.par[i])

    def connect(self, i, j):
        i, j = self.get_root(i), self.get_root(j)

        if i != j:
            if self.sz[i] < self.sz[j]: i, j = j, i
            self.par[j] = i
            self.sz[i] += self.sz[j]

            if self.cur[i] == self.cur[j]:
                r = self.cnt[i] * self.cnt[j]
                self.cnt[i] += self.cnt[j]
                return r

            elif self.cur[i] < self.cur[j]:
                self.cur[i], self.cnt[i] = self.cur[j], self.cnt[j]

        return 0

    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        self.sz = [1] * n
        self.cur = vals
        self.cnt = [1] * n
        self.par = list(range(n))
        return sum([self.connect(a, b) for a, b in sorted(edges, key=lambda p: max(vals[p[0]], vals[p[1]]))]) + n