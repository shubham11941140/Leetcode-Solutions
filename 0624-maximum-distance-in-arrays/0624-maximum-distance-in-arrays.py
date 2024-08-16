class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        max_distance = 0
        
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_distance = max(max_distance, abs(arr[-1] - min_val), abs(max_val - arr[0]))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        
        return max_distance        