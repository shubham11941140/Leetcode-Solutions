class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane(nums):
            cur_sum = max_sum = nums[0]
            for num in nums[1:]:
                cur_sum = max(num, cur_sum + num)
                max_sum = max(max_sum, cur_sum)
            return max_sum

        # If all elements are negative, return the max element
        if all(num < 0 for num in nums):
            return max(nums)

        # Find the maximum subarray sum
        max_sum = kadane(nums)

        # Find the minimum subarray sum
        min_sum = kadane([-num for num in nums])
        
        print(max_sum, min_sum)

        # Find the maximum subarray sum circular
        max_sum_circular = sum(nums) + min_sum
        return max(max_sum, max_sum_circular) 