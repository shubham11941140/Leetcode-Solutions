class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([1 for i in grid for j in i if j < 0])
