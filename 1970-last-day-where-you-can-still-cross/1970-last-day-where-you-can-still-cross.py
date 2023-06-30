class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def is_possible(mid):
            grid = [[0] * col for _ in range(row)]
            for i in range(mid):
                r, c = cells[i][0] - 1, cells[i][1] - 1
                grid[r][c] = 1
            
            # Perform a DFS to check if there is a path from any cell in the first row to any cell in the last row
            def dfs(r, c):
                if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 0:
                    return False
                if r == row - 1:
                    return True
                
                grid[r][c] = 2  # Mark cell as visited
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if dfs(r + dr, c + dc):
                        return True
                
                return False
            
            # Start DFS from the cells in the first row
            for c in range(col):
                if dfs(0, c):
                    return True
            
            return False
        
        left, right = 0, len(cells)
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            if is_possible(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans        