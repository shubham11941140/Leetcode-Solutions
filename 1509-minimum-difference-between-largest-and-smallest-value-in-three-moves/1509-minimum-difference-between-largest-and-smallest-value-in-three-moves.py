class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        if n <= 3:
            return 0
        return min([nums[n - 4 + i] - nums[i] for i in range(4)])
      