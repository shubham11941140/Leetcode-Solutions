class Solution:

    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]  # Track the smallest value seen so far
        max_diff = -1  # Default to -1 if no valid pair is found
        for num in nums[1:]:  # Start from the second element
            if num > min_val:
                max_diff = max(max_diff, num - min_val)
            min_val = min(min_val, num)  # Update min_val
        return max_diff
