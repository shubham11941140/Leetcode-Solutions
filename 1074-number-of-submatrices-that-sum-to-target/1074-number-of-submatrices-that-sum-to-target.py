class Solution:

    def numSubmatrixSumTarget(self, matrix: List[List[int]],
                              target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ms = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not i and not j:
                    ms[i][j] = matrix[i][j]
                elif not i:
                    ms[i][j] = matrix[i][j] + ms[i][j - 1]
                elif not j:
                    ms[i][j] = matrix[i][j] + ms[i - 1][j]
                else:
                    ms[i][j] = (matrix[i][j] + (ms[i][j - 1]) +
                                (ms[i - 1][j]) - (ms[i - 1][j - 1]))
        ans = 0
        for y1 in range(m):
            for y2 in range(y1, m):
                ss = defaultdict(int)
                ss[0] = 1
                for x in range(n):
                    msum = ms[y2][x]
                    if y1:
                        msum -= ms[y1 - 1][x]
                    if msum - target in ss:
                        ans += ss[msum - target]
                    ss[msum] += 1
        return ans
