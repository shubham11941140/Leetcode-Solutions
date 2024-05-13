class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        A = grid.copy()
        M, N = len(A), len(A[0])
        res = (1 << (N - 1)) * M  # The left-most column is all 1s

        for j in range(1, N):
            # Count the number of 1s in the j-th column
            ones = sum(A[i][j] == A[i][0] for i in range(M))
            # Flip the column if the number of 1s is less than M / 2
            res += max(ones, M - ones) * (1 << (N - 1 - j))

        return res
