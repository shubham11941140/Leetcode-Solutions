class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min([rgt - lft for lft, rgt in zip(nums, nums[k - 1:])])