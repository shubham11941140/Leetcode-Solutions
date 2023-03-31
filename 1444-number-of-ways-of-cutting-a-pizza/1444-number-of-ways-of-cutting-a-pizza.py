class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        r, c = len(pizza), len(pizza[0])
        g = [[0] * (c + 1) for _ in range(r + 1)]
        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                g[i][j] = (
                    g[i + 1][j] + g[i][j + 1] -
                    g[i + 1][j + 1] + (pizza[i][j] == "A")
                )

        @lru_cache(None)
        def dp(i, j, k):
            if g[i][j] == 0:
                return 0
            if k == 0:
                return 1
            ans = 0
            for x in range(i + 1, r):
                if g[i][j] - g[x][j] > 0:
                    ans += dp(x, j, k - 1)
                    ans %= mod
            for y in range(j + 1, c):
                if g[i][j] - g[i][y] > 0:
                    ans += dp(i, y, k - 1)
                    ans %= mod
            return ans

        return dp(0, 0, k - 1)
