class Solution:

    @staticmethod
    def searchInsert(nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        for i, item in enumerate(nums):
            if item > target:
                return i
        return len(nums)
