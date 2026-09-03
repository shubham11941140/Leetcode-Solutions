class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True if len([i for i in nums1 if i % 2]) in [0, len(nums1)] else bool(min(nums1) % 2)