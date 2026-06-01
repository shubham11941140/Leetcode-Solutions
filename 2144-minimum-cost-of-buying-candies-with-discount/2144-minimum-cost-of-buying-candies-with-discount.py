class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        s = 0
        n = len(cost)
        for i in range(n):
            if i % 3 == 2:
                s += cost[i]
        return sum(cost) - s
        