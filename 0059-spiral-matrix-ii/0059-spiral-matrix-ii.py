class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0 for i in range(n)] for j in range(n)]
        v = [[False for i in range(n)] for j in range(n)]
        c = 1
        for var in range(n):                    
            for x in range(n):
                if not v[var][x]:
                    mat[var][x] = c
                    v[var][x] = True
                    c += 1
            for y in range(n):
                if not v[y][n - 1 - var]:
                    mat[y][n - 1 - var] = c
                    v[y][n - 1 - var] = True
                    c += 1
            for x in reversed(range(n)):
                if not v[n - 1 - var][x]:
                    mat[n - 1 - var][x] = c
                    v[n - 1 - var][x] = True
                    c += 1
            for y in reversed(range(n)):
                if not v[y][var]:
                    mat[y][var] = c
                    v[y][var] = True
                    c += 1 
        return mat        