class Solution:

    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return 0 if n <= 3 else min([nums[n - 4 + i] - nums[i] for i in range(4)])
