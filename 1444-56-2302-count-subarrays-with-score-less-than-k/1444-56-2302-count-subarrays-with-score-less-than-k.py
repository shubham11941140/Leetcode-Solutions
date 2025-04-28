class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        current_sum = 0
        left = 0
        for right in range(n):
            current_sum += nums[right]            
            # Adjust the window until the condition is satisfied
            while current_sum * (right - left + 1) >= k and left <= right:
                current_sum -= nums[left]
                left += 1            
            # Add the count of valid subarrays ending at 'right'
            count += (right - left + 1)        
        return count   