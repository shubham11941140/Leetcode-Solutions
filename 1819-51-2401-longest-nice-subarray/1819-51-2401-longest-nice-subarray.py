class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 0
        current_mask = 0
        left = 0
        for right in range(n):
            # Ensure the current subarray is "nice"
            while current_mask & nums[right]:
                current_mask ^= nums[left]
                left += 1
            # Add the current number to the mask
            current_mask |= nums[right]
            # Update the maximum length
            max_length = max(max_length, right - left + 1)
        return max_length       