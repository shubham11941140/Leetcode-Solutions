class Solution:
    

    
    
    @cache
    def bfs(self):        
        while self.q:
            i, j = self.q.pop(0)
            self.v[i][j] = True
            if 0 in [i, j]:
                self.p = True
            if i == self.n - 1 or j == self.m - 1:
                self.a = True
            if self.p and self.a:
                break
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= x < self.n and 0 <= y < self.m:
                    if self.h[x][y] <= self.h[i][j]:
                        if not self.v[x][y]:
                            self.q.append((x, y))
            
    def dfs(self, v, i, j, val):
        if i < 0 or j < 0 or i >= self.n or j >= self.m:
            return
        if self.h[i][j] < val:
            return
        if v[i][j]:
            return
        v[i][j] = True
        for x, y in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
            self.dfs(v, x, y, self.h[i][j])
        
    
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS at each cell check whether we reach limits
        self.n = len(heights)
        self.m = len(heights[0])
        self.h = heights
        a = [[False for i in range(self.m)] for j in range(self.n)]
        p = [[False for i in range(self.m)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                if i == 0 or j == 0:
                    self.dfs(a, i, j, 0)
                if i == self.n - 1 or j == self.m - 1:
                    self.dfs(p, i, j, 0)
        print("A", a)
        print("P", p)
        ans = []
        for i in range(self.n):
            for j in range(self.m):
                if a[i][j] and p[i][j]:
                    print(i, j)
                    ans.append([i, j])
        return ans

                
                
        