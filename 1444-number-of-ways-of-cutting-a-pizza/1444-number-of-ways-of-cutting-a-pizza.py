class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        r, c = len(pizza), len(pizza[0])
        g = [[0] * (c + 1) for _ in range(r + 1)]
        for i in reversed(range(r)):
            for j in reversed(range(c)):
                g[i][j] = (
                    g[i + 1][j] + g[i][j + 1] -
                    g[i + 1][j + 1] + (pizza[i][j] == "A")
                )

        @lru_cache(None)
        def dp(i, j, k):
            if not g[i][j]:
                return 0
            if not k:
                return 1
            return (
                sum([dp(x, j, k - 1)
                    for x in range(i + 1, r) if g[i][j] > g[x][j]])
                + sum([dp(i, y, k - 1)
                      for y in range(j + 1, c) if g[i][j] > g[i][y]])
            ) % (10**9 + 7)

        return dp(0, 0, k - 1)
