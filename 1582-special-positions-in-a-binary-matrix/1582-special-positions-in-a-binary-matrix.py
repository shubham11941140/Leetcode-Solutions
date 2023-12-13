class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        rows = [0] * n
        cols = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
        return sum([1 for i in range(n) for j in range(m) if mat[i][j] == 1 and rows[i] == 1 and cols[j] == 1])
        