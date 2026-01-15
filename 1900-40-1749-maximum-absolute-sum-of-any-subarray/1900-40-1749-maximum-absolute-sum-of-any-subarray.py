class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = min_sum = 0
        max_res = min_res = 0
        for num in nums:
            max_sum = max(num, max_sum + num)
            min_sum = min(num, min_sum + num)
            max_res = max(max_res, max_sum)
            min_res = min(min_res, min_sum)
        return max(max_res, abs(min_res))
