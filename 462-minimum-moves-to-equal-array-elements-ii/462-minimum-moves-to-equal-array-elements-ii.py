class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        m = sorted(nums)[len(nums) // 2]
        return sum(abs(i - m) for i in nums)        
