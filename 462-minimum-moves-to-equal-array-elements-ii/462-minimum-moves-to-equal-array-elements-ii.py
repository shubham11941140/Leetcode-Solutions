class Solution:

    @staticmethod
    def minMoves2(nums: List[int]) -> int:
        m = sorted(nums)[len(nums) // 2]
        return sum(abs(i - m) for i in nums)
