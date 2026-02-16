class Solution:

    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        nums.append(-1)
        for i in range(1, len(nums)):
            if nums[i - 1] >= i > nums[i]:
                return i
        return -1
