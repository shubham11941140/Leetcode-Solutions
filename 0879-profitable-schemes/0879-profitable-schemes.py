class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        dp = [[[0 for _ in range(minProfit + 1)] for _ in range(n + 1)] for _ in range(len(group) + 1)]
        for i in range(n + 1):
            dp[0][i][0] = 1
        for i in range(1, len(group) + 1):
            for j in range(n + 1):
                for k in range(minProfit + 1):
                    if j < group[i - 1]:
                        dp[i][j][k] = dp[i - 1][j][k]
                    else:
                        dp[i][j][k] = dp[i - 1][j][k] + dp[i - 1][j - group[i - 1]][max(0, k - profit[i - 1])]
        return dp[-1][-1][-1] % (10**9 + 7)