class Solution:

    @staticmethod
    def minDistance(X: str, Y: str) -> int:
        m = len(X)
        n = len(Y)
        L = [[0] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                L[i][j] = (L[i - 1][j - 1] + 1 if X[i - 1] == Y[j - 1] else
                           max(L[i - 1][j], L[i][j - 1]))
        return (m + n) - (2 * L[m][n])
