class Solution:

    def canSortArray(self, nums: List[int]) -> bool:
        for _ in range(len(nums)):
            for i in range(len(nums) - 1):
                if (
                    bin(nums[i]).count("1") == bin(nums[i + 1]).count("1")
                    and nums[i + 1] < nums[i]
                ):
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums == sorted(nums)
