class Solution:

    @staticmethod
    def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        j = len(nums2)
        nums1 += nums2
        for _ in range(j):
            nums1.remove(0)
        nums1.sort()
