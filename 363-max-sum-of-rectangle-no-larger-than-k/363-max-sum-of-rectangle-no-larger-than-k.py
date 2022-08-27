from bisect import bisect_left, insort
from copy import deepcopy


class Solution:
    @staticmethod
    def transpose(m):
        return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]

    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:

        if len(matrix) > len(matrix[0]):
            matrix = self.transpose(matrix)

        r = len(matrix)
        c = len(matrix[0])

        pm = deepcopy(matrix)

        for i in range(r):
            for j in range(c):
                if i:
                    pm[i][j] += pm[i - 1][j]
                if j:
                    pm[i][j] += pm[i][j - 1]
                if i and j:
                    pm[i][j] -= pm[i - 1][j - 1]

        ret = float("-inf")
        for f in range(r):
            for l in range(f, r):
                ss = [0]
                for j in range(c):
                    ns = pm[l][j] - (pm[f - 1][j] if f else 0)
                    ind = bisect_left(ss, ns - k)
                    if ind < len(ss):
                        ret = max(ret, ns - ss[ind])
                        if ret == k:
                            return ret
                    insort(ss, ns)
        return ret
