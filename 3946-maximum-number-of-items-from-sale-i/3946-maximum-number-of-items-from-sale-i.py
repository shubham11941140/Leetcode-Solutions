class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        bonus = [0] * n
        for i in range(n):
            bonus[i] = len([1 for j in range(n) if i != j and items[j][0] % items[i][0] == 0])
        dp = [0] * (budget + 1)
        for i in range(n):
            cost = items[i][1]
            if cost <= budget:
                for b in range(budget, cost - 1, -1):
                    dp[b] = max(dp[b], dp[b - cost] + 1 + bonus[i])
                for b in range(cost, budget + 1):
                    dp[b] = max(dp[b], dp[b - cost] + 1)
        return max(dp)