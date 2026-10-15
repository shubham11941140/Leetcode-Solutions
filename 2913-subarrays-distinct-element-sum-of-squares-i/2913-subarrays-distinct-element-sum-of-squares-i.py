class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        return sum((seen.add(x) or len(seen)) ** 2 for i in range(len(nums)) for seen in [set()] for x in nums[i:])