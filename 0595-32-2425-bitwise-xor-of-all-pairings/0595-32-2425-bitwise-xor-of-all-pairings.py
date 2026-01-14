class Solution:

    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        return (len(nums1) % 2 * reduce(xor, nums2)) ^ (len(nums2) % 2 *
                                                        reduce(xor, nums1))
