class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        c0 = nums.count(0)
        c1 = nums.count(1)
        c2 = nums.count(2)
        for i in range(c0):
            nums[i] = 0
        for i in range(c0, c0 + c1):
            nums[i] = 1
        for i in range(c0 + c1, n):
            nums[i] = 2
            
            