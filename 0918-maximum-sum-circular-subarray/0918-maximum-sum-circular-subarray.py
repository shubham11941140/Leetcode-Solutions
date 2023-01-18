class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadane's algorithm
        def kadane(nums):
            cur_sum = max_sum = nums[0]
            for num in nums[1:]:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        # If all elements are negative, return the max element
        if all(num < 0 for num in nums):
            return max(nums)

        return max(kadane(nums), sum(nums) + kadane([-num for num in nums]))