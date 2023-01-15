class Solution:

    def get_root(self, i):
        if i == self.par[i]:
            return i
        return self.get_root(self.par[i])

    def numberOfGoodPaths(self, vals: List[int],
                          edges: List[List[int]]) -> int:

        def connect(i, j):
            i, j = self.get_root(i), self.get_root(j)

            if i != j:
                if sz[i] < sz[j]:
                    i, j = j, i
                self.par[j] = i
                sz[i] += sz[j]

                if cur[i] == cur[j]:
                    r = cnt[i] * cnt[j]
                    cnt[i] += cnt[j]
                    return r

                elif cur[i] < cur[j]:
                    cur[i], cnt[i] = cur[j], cnt[j]
            return 0

        n = ans = len(vals)
        sz, cur, cnt = [1] * n, vals, [1] * n
        self.par = list(range(n))

        for a, b in sorted(edges, key=lambda p: max(vals[p[0]], vals[p[1]])):
            ans += connect(a, b)

        return ans
