class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        l = len(a) // 2 
        return a[l] if len(a) % 2 else (a[l] + a[l - 1]) / 2

        