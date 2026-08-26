class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            grid2[i][j] = 0
            is_sub_island = grid1[i][j] == 1
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i, j - 1)
            is_sub_island &= dfs(i, j + 1)
            return is_sub_island

        m, n = len(grid1), len(grid2[0])
        return len([1 for i in range(m) for j in range(n) if grid2[i][j] if dfs(i, j)])
