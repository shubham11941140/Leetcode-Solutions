class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums2)
        s = set(nums1)
        return [i for i in s if i in c]
