class Solution:

    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        z = [i for i in range(n) if not nums[i]]
        lz = len(z)
        if not z or lz == 1:
            return n - 1
        ls = 0
        ls = max(ls, z[1] - 1, n - z[-2] - 2)
        for i in range(1, lz - 1):
            ls = max(ls, z[i + 1] - z[i - 1] - 2)
        return ls
