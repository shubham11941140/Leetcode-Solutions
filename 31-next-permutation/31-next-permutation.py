class Solution:

    def findMaxIndex(self, index, a, curr):
        ans = -1
        index = 0
        for i in range(index, len(a)):
            if a[i] > curr:
                ans = curr if ans == -1 else min(ans, a[i])
                index = i
        return index

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        f = False
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                f = True
                break
        if not f:
            nums.sort()
        else:
            m = self.findMaxIndex(i + 1, nums, nums[i])
            nums[i], nums[m] = nums[m], nums[i]
            nums[i + 1:] = nums[i + 1:][::-1]
