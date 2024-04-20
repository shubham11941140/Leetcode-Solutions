class Solution:

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m, n = len(land), len(land[0])
        res = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    x, y = i, j
                    while x < m and land[x][j] == 1:
                        x += 1
                    while y < n and land[i][y] == 1:
                        y += 1
                    for p in range(i, x):
                        for q in range(j, y):
                            land[p][q] = 0
                    res.append([i, j, x - 1, y - 1])
        return res
