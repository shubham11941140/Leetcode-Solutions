class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        def dfs(i, j):
            # If out of bounds or it's water in grid2, return True (base case)
            if i < 0 or i >= m or j < 0 or j >= n or grid2[i][j] == 0:
                return True
            # Mark this cell as visited by setting it to 0
            grid2[i][j] = 0
            # Check if this cell is part of a valid sub-island
            is_sub_island = grid1[i][j] == 1
            # Explore all four directions (up, down, left, right)
            is_sub_island &= dfs(i - 1, j)
            is_sub_island &= dfs(i + 1, j)
            is_sub_island &= dfs(i, j - 1)
            is_sub_island &= dfs(i, j + 1)
            return is_sub_island

        m, n = len(grid1), len(grid2[0])
        sub_island_count = 0

        for i in range(m):
            for j in range(n):
                if (
                    grid2[i][j] == 1
                ):  # Start a DFS if we find an unvisited island in grid2
                    if dfs(i, j):
                        sub_island_count += 1

        return sub_island_count
