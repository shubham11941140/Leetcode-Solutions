class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches, i, max_reach = 0, 0, 1
        while max_reach <= n:
            if i < len(nums) and nums[i] <= max_reach:
                max_reach += nums[i]
                i += 1
            else:
                max_reach += max_reach
                patches += 1
        return patches        