class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        if not img or not img[0]: 
            return []
        m, n = len(img), len(img[0])
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                count = 0
                for a in dx: 
                    for b in dy:
                        if 0 <= i + a < m and 0 <= j + b < n:
                            res[i][j] += img[i+a][j+b]
                            count += 1
                res[i][j] //= count
        return res        