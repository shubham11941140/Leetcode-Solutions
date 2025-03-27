class Solution:
    def minimumIndex(self, nums: List[int]) -> int:       
        # Get the dominant element of the entire array
        dominant, total_freq = max(Counter(nums).items(), key = lambda x: x[1])        
        left_freq = 0
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left_freq += 1
            right_freq = total_freq - left_freq            
            if left_freq > (i + 1) // 2 and right_freq > (len(nums) - (i + 1)) // 2:
                return i        
        return -1  # No valid split found      