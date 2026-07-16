class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        b = sorted(map(gcd, nums, accumulate(nums, max)))
        return sum(map(gcd, b[:len(b) // 2], b[::-1]))