class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]
        m = len(cuts)
        dp = [[0] * m for _ in range(m)]
        for d in range(2, m):
            for i in range(m - d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(i + 1, j))
                dp[i][j] += cuts[j] - cuts[i]
        return dp[0][-1]     