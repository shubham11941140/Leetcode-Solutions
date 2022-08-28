class Solution:

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        s = set([(i - j) for i in range(n) for j in range(m)])
        for k in s:
            b = sorted(
                [mat[i][j] for i in range(n) for j in range(m) if i - j == k])
            c = 0
            for i in range(n):
                for j in range(m):
                    if i - j == k:
                        mat[i][j] = b[c]
                        c += 1
        return mat
