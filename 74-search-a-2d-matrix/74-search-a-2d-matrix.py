class Solution:

    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if j > target:
                    return False
                if j == target:
                    return True
