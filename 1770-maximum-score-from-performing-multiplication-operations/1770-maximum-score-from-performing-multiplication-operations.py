class Solution:
    def maximumScore(self, num: List[int], mul: List[int]) -> int:        
        n = len(num)
        m = len(mul)
        d = [[0] * (m + 1) for i in range(m + 1)]
        for j in reversed(range(m)):
            for l in reversed(range(j + 1)):
                d[j][l] = max(num[l] * mul[j] + d[j + 1][l + 1], num[n - 1 - (j - l)] * mul[j] + d[j + 1][l])
        return d[0][0]
        