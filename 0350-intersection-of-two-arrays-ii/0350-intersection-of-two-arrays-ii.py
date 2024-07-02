class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        result = []
        for num in nums2:
            if counter[num] > 0:
                result.append(num)
                counter[num] -= 1
        return result        