class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        stab = []
        n = len(nums)
        for i in range(n):
            m1 = max(nums[:i + 1])
            m2 = min(nums[i:])
            if m1 - m2 <= k:
                return i
        return -1