class Solution:

    def countPartitions(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        count = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            if left_sum % 2 == (total_sum - left_sum) % 2:
                count += 1
        return count
