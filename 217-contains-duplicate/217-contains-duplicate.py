class Solution:

    @staticmethod
    def containsDuplicate(nums: List[int]) -> bool:
        return not len(set(nums)) == len(nums)
