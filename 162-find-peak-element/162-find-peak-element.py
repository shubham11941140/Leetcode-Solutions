class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i
        # Check at 1 and n - 1
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[-2] < nums[-1]:
            return len(nums) - 1
