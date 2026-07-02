class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        @lru_cache(None)
        def dp(x: int, y: int, health_used: int)-> int: 
            if health_used == health or (x, y) not in eligible: 
                return inf
            cnt = health_used + grid[x][y]
            if (x, y) == (m - 1 , n - 1): 
                return cnt        
            eligible.discard((x, y))
            res = min(dp(x + 1, y, cnt), dp(x, y + 1, cnt),
                      dp(x - 1, y, cnt), dp(x, y - 1, cnt))
            eligible.add((x, y))
            return res

        m, n = len(grid), len(grid[0])
        eligible = set(product(range(m), range(n)))
        return dp(0,0,0) < health                