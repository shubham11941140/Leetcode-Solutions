class Solution:
    def maxSum(self, nums: List[int]) -> int:
        return max(nums) if all(n < 0 for n in nums) else sum(n for n in set(nums) if n > 0)        