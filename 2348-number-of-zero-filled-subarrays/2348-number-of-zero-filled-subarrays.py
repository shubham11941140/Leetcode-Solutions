class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                count = 0
            nums[i] = count
        return sum(nums)     