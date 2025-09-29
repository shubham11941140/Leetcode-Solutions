class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        return (f := cache(lambda i, j: j - i > 1 and min(f(i, k) + values[i] * values[k] * values[j] + f(k, j) for k in range(i + 1, j))))(0, len(values) - 1)