class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(curr: int, rem: int) -> int:
            if rem < 0:
                return 0
            else:
                result = int(curr == finish)
            for loc in range(len(locations)):                    
                if curr != loc:
                    cost = abs(locations[curr] - locations[loc])
                    result += dfs(loc, rem - cost)
            return result        
        return dfs(start, fuel) % (10 ** 9 + 7)   