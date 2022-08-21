class Solution:
    
    @cache
    def dp(self, i, p, h):
        if (h > self.t) or (i == self.m and h != self.t):
            return self.inf
        if i == self.m:
            return 0
        if self.h[i]:
            return self.dp(i + 1, self.h[i], h + int(p != self.h[i]))
        best = self.inf
        for j, c in enumerate(self.c[i], 1):
            best = min(best, self.dp(i + 1, j, h + int(p != j)) + c)
        return best    
    
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        self.h = houses
        self.c = cost
        self.m = m
        self.n = n
        self.t = target
        self.inf = 10 ** 10
        res = self.dp(0, 0, 0)
        return res if res != self.inf else -1
