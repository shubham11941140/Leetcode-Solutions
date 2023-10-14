class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        @lru_cache(None)  # Using lru_cache for memoization
        def calc(ctime, index):
            if ctime >= n:
                return 0
            if index == n:
                return 10**20

            return min(
                calc(ctime + time[index] + 1, index + 1) + cost[index],
                calc(ctime, index + 1),
            )

        return min(10**20, calc(0, 0))
