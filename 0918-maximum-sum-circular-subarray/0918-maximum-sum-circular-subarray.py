class Solution:

    def kadane(self, nums):
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
        return max_sum

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        return (max(nums) if max(nums) < 0 else max(
            self.kadane(nums),
            sum(nums) + self.kadane([-num for num in nums])))
