class Solution:
    def check(self, nums: List[int]) -> bool:
        return len([i for i in range(len(nums)) if nums[i] > nums[(i + 1) % len(nums)]]) <= 1        