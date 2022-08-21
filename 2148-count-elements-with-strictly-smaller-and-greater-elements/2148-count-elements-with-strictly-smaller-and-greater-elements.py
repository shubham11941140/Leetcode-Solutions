class Solution:

    @staticmethod
    def countElements(nums: List[int]) -> int:
        return max(0,
                   len(nums) - (nums.count(min(nums)) + nums.count(max(nums))))
