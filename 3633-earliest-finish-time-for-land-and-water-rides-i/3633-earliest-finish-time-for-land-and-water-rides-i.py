class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans = float('inf')
        # Try every land-water ride pair
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                # Case 1: Land -> Water
                land_finish = landStartTime[i] + landDuration[i]
                finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]
                # Case 2: Water -> Land
                water_finish = waterStartTime[j] + waterDuration[j]
                finish2 = max(water_finish, landStartTime[i]) + landDuration[i]
                # Update answer
                ans = min(ans, finish1, finish2)
        return ans     