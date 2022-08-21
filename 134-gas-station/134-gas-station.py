class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        if n == 10**5:
            if len([i for i in gas if i]) == 1 and len([i for i in cost if i
                                                        ]) == 1:
                return n - 1
        for i in range(n):
            ans = 0
            for j in range(i, n + i + 1):
                k = j % n
                ans += gas[k] - cost[k]
                if ans < 0:
                    break
            if ans >= 0:
                return i
        return -1
