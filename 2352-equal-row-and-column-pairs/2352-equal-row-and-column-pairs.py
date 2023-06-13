class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return len([1 for i in grid for k in range(len(grid)) if i == [grid[j][k] for j in range(len(grid))]])
                    
        