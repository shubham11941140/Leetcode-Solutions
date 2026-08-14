class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]
        return max(max_sum, current_sum)
