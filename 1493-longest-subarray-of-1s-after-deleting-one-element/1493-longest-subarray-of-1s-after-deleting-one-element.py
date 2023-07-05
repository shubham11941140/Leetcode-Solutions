class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        z = [i for i in range(n) if not nums[i]]
        lz = len(z)
        if not z or lz == 1:
            return n - 1
        ls = 0
        for i in range(lz):
            if i == 0:
                ss = (z[i + 1] - z[i] - 1) + z[i]
            if 0 < i < lz - 1:
                ss = (z[i] - z[i - 1] - 1) + (z[i + 1] - z[i] - 1) 
            if i > 0 and i == lz - 1:
                ss = (z[i] - z[i - 1] - 1) + (n - z[i] - 1)
            ls = max(ls, ss)            
        return ls
        