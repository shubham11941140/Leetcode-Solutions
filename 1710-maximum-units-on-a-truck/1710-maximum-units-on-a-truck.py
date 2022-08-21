class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for number, units in boxTypes:
            if truckSize <= 0:
                break
            if truckSize >= number:
                ans += number * units
                truckSize -= number
            elif 0 < truckSize < number:
                ans += truckSize * units
                break
        return ans
