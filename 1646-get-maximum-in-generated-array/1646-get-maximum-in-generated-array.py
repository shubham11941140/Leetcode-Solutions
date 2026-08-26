class Solution:

    def getMaximumGenerated(self, n: int) -> int:
        nums = [0 for i in range(2 * n + 100)]
        nums[1] = 1
        for i in range(n):
            nums[2 * i] = nums[i]
            nums[2 * i + 1] = nums[i] + nums[i + 1]
        return max(nums[:n + 1])
