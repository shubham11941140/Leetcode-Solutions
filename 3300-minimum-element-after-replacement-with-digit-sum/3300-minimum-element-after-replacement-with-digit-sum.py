class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min([sum([int(j) for j in str(i)]) for i in nums])                