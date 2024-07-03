class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        if n <= 3:
            return 0

        # Try out all four scenarios for modifications
        ans = float('inf')
        for i in range(4):
            ans = min(ans, nums[n - 4 + i] - nums[i])

        return ans        