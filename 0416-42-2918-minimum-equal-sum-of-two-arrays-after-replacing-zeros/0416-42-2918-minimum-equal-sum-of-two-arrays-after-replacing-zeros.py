class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, sum2 = sum(nums1), sum(nums2)
        zeros1, zeros2 = nums1.count(0), nums2.count(0)
        if zeros1 == 0 and zeros2 == 0:
            return sum1 if sum1 == sum2 else -1
        elif zeros1 == 0:
            return sum1 if sum2 + zeros2 <= sum1 else -1
        elif zeros2 == 0:
            return sum2 if sum1 + zeros1 <= sum2 else -1
        return max(sum1 + zeros1, sum2 + zeros2)