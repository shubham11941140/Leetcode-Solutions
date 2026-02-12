class Solution:

    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        r = n - 1
        ans = 0
        while l < r:
            ans = max(nums[l] + nums[r], ans)
            l += 1
            r -= 1
        return ans
