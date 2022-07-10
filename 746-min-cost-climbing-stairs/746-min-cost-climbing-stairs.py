class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(n + 1)]
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n + 1):
            if 0 <= i < n:
                dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]
            else:
                dp[i] = min(dp[i - 2], dp[i - 1]) 
        print(dp)
        return dp[-1]
        