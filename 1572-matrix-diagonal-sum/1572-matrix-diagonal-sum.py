class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum([mat[i][j] for i in range(len(mat)) for j in range(len(mat)) if j in [i, len(mat) - 1 - i]])
