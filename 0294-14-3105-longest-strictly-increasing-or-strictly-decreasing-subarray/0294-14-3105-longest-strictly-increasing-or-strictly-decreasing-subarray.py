class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:        
        l = 1
        ci = 1
        cd = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                ci, cd = ci + 1, 1
            elif nums[i] < nums[i - 1]:
                cd, ci = cd + 1, 1
            else:
                cd, ci = 1, 1
            l = max(l, cd, ci)
        return l