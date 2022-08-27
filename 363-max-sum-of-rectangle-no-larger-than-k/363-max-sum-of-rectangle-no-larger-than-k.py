import bisect
from copy import deepcopy


class Solution:
    @staticmethod
    def transpose(matrix):
        return [
            [matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))
        ]

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        if len(matrix) > len(matrix[0]):
            matrix = self.transpose(matrix)

        numRows = len(matrix)
        numCols = len(matrix[0])

        partialSumMatrix = deepcopy(matrix)

        for i in range(numRows):
            for j in range(numCols):
                if i > 0:
                    partialSumMatrix[i][j] += partialSumMatrix[i - 1][j]
                if j > 0:
                    partialSumMatrix[i][j] += partialSumMatrix[i][j - 1]
                if i > 0 and j > 0:
                    partialSumMatrix[i][j] -= partialSumMatrix[i - 1][j - 1]

        # enumerate all first and last rows, then determine best among different cols
        ret = float("-inf")
        for firstRow in range(numRows):
            for lastRow in range(firstRow, numRows):
                sortedSums = [0]

                for j in range(numCols):
                    nextSum = partialSumMatrix[lastRow][j] - (
                        partialSumMatrix[firstRow -
                                         1][j] if firstRow > 0 else 0
                    )
                    ind = bisect.bisect_left(sortedSums, nextSum - k)
                    if ind < len(sortedSums):
                        ret = max(ret, nextSum - sortedSums[ind])
                        if ret == k:  # shortcut
                            return ret
                    bisect.insort(sortedSums, nextSum)

        return ret
