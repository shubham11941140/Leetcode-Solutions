class Solution:

    @staticmethod
    def searchMatrix(matrix: List[List[int]], target: int) -> bool:
        return any(target in i for i in matrix)
