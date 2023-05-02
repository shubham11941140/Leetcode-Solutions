class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            l = len([1 for i in nums if i < 0])
            if l % 2:
                return -1
            else:
                return 1
        