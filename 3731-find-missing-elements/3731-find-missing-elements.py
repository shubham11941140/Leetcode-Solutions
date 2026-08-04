class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return [i for i in list(range(min(nums), max(nums))) if i not in nums]        