class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])    
        t = [0] * (n + 1)
        b = [0] * (n + 1)    
        for i in range(n):
            t[i + 1] = t[i] + grid[0][i]
            b[i + 1] = b[i] + grid[1][i]         
        return min([max(t[n] - t[i + 1], b[i]) for i in range(n)])  