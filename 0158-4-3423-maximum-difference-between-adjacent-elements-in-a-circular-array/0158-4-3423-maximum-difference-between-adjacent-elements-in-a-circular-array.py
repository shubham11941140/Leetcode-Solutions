class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = max([abs(nums[i] - nums[i + 1]) for i in range(n - 1)])
        max_diff = max(max_diff, abs(nums[0] - nums[-1]))
        return max_diff  