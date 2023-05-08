class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if (i == j) or (j == len(mat) - 1 - i):
                    result += mat[i][j]
        return result
