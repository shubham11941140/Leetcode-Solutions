class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        print(boxTypes)
        i = 0 
        n = len(boxTypes)
        ans = 0
        while i < n:
            number, units = boxTypes[i]
            print(truckSize, number, units)
            if truckSize <= 0:
                break
            if truckSize >= number:
                ans += (number * units)
                truckSize -= number
            elif 0 < truckSize < number:
                ans += (truckSize * units)
                break
            i += 1
        return ans
        