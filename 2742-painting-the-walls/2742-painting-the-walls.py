class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)  # Using lru_cache for memoization
        def calc(ctime, i):
            if ctime >= n:
                return 0
            if i == n:
                return 10**20

            return min(calc(ctime + time[i] + 1, i + 1) + cost[i], calc(ctime, i + 1))

        return min(10**20, calc(0, 0))
