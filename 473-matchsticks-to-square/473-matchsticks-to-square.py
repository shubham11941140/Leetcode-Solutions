class Solution:

    @cache
    def dfs(self, a, b, c, d, idx):
        if max(a, b, c, d) > self.k:
            return False
        if idx == self.l:
            if a == b == c == d == self.k:
                return True
            return False
        t = self.m[idx]
        if (self.dfs(a + t, b, c, d, idx + 1)
                or self.dfs(a, b + t, c, d, idx + 1)
                or self.dfs(a, b, c + t, d, idx + 1)
                or self.dfs(a, b, c, d + t, idx + 1)):
            return True
        return False

    def makesquare(self, matchsticks: List[int]) -> bool:
        n = sum(matchsticks)
        self.l = len(matchsticks)
        if n % 4:
            return False
        else:
            self.k = n // 4
            idx = 0
            self.m = sorted(matchsticks, reverse=True)
            return self.dfs(0, 0, 0, 0, idx)
