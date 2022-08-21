class Solution:

    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        l = len(a) // 2
        if len(a) % 2:
            return a[l]
        return (a[l] + a[l - 1]) / 2
