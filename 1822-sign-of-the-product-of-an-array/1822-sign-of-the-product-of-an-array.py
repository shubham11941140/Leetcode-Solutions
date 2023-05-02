class Solution:

    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            return -1 if len([1 for i in nums if i < 0]) % 2 else 1
