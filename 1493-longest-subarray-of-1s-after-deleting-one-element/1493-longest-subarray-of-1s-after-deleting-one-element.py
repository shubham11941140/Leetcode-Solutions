class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        z = [i for i in range(n) if not nums[i]]
        lz = len(z)
        if not z or lz == 1:
            return n - 1
        ls = 0
        ss = z[1] - 1
        ls = max(ls, ss)
        ss = n - z[-2] - 2
        ls = max(ls, ss)
        for i in range(1, lz - 1):
            ss = (z[i] - z[i - 1] - 1) + (z[i + 1] - z[i] - 1)
            ls = max(ls, ss)
        return ls
