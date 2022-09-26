class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        res = float('-inf')
        for i in nums:
            curr = max(curr + i, i)
            res = max(res, curr)
        return res        