class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(curr: int, remaining_fuel: int) -> int:
            if remaining_fuel < 0:
                return 0
            else:
                result = int(curr == finish)
            for next_loc in range(len(locations)):                    
                if curr != next_loc:
                    cost = abs(locations[curr] - locations[next_loc])
                    result += dfs(next_loc, remaining_fuel - cost)
            return result
        
        return dfs(start, fuel) % (10 ** 9 + 7)   