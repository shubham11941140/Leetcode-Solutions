class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        M = img.copy()
        if not M or not M[0]: return []
        m, n = len(M), len(M[0])
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for a in dx:
                    for b in dy:
                        if 0 <= i+a < m and 0 <= j+b < n:
                            res[i][j] += M[i+a][j+b]
                            count += 1
                res[i][j] //= count
        return res        