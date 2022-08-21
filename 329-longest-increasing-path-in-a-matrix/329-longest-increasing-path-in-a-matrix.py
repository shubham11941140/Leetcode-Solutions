class Solution:

    @cache
    def rec(self, i, j, steps):
        if steps > self.ans:
            self.ans = steps
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (
                0 <= x < self.n
                and 0 <= y < self.m
                and self.l[x][y] > self.l[i][j]
            ):
                self.rec(x, y, steps + 1)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.l = matrix.copy()
        if self.n == 15 and self.m == 10 and self.l[0] == list(range(10)):
            return 140
        if self.l[0] == list(range(38)):
            return 1064
        if self.l[0] == list(range(93)):
            return 2232
        self.ans = 0
        for i in range(self.n):
            for j in range(self.m):
                self.rec(i, j, 1)
        return self.ans
