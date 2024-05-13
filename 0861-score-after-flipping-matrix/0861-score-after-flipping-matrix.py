class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        A = grid.copy()
        M, N = len(A), len(A[0])
        res = (1 << (N - 1)) * M
        for j in range(1, N):
            ones = sum(A[i][j] == A[i][0] for i in range(M))
            res += max(ones, M - ones) * (1 << (N - 1 - j))
        return res        