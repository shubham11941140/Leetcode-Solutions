class Solution:

    def divideArray(self, nums: List[int]) -> bool:
        return 1 not in [v % 2 for v in Counter(nums).values()]
