class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        first_price = prices[0]
        dp = [[0, -first_price, first_price] for _ in range(k + 1)]
        n = len(prices)        
        for day in range(1, n):
            cp = prices[day]
            for t in range(k, 0, -1):
                dp[t][0] = max(dp[t][0], dp[t][1] + cp, dp[t][2] - cp)
                dp[t][1] = max(dp[t][1], dp[t - 1][0] - cp)
                dp[t][2] = max(dp[t][2], dp[t - 1][0] + cp)        
        return dp[k][0]        