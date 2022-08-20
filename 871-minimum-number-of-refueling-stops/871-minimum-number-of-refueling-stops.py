class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        
        n = len(stations)
        dp = [0 for i in range(n + 1)]
        dp[0] = startFuel
        for i in range(n):
            for j in reversed(range(i + 1)):
                if dp[j] >= stations[i][0]:
                    dp[j + 1] = max(dp[j + 1], dp[j] + stations[i][1])        
        for i in range(n + 1):
            if dp[i] >= target:
                return i
        return -1
        