class Solution:
    
    @cache
    def move(self, m, r, c):
        if not ((0 <= r < self.m) and (0 <= c < self.n)):
            return 1
        if not m:
            return 0        
        m -= 1
        return self.move(m, r - 1, c) + self.move(m, r + 1, c) + self.move(m, r, c - 1) + self.move(m, r, c + 1)
        
    
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        self.m = m
        self.n = n
        return self.move(maxMove, startRow, startColumn) % (10 ** 9 + 7)
        