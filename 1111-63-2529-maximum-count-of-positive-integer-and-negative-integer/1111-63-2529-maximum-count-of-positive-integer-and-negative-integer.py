class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len([i for i in nums if i > 0]), len([i for i in nums if i < 0]))        