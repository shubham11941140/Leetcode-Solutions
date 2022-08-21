class Solution:

    @staticmethod
    def check(i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                t = 0
                s = 0
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if self.check(x, y, n, m):
                        t += 1
                        if mat[i][j] > mat[x][y]:
                            s += 1
                if t == s:
                    return [i, j]
