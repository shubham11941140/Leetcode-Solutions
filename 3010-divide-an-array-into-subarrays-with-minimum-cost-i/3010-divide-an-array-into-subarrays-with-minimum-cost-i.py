class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums[1:] = sorted(nums[1:])
        return ans + nums[1] + nums[2]