class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        s = sorted(nums)
        if s == nums:
            return 0
        l = 0
        r = n - 1
        while s[l] == nums[l]:
            l += 1
        while s[r] == nums[r]:
            r -= 1
        return r - l + 1