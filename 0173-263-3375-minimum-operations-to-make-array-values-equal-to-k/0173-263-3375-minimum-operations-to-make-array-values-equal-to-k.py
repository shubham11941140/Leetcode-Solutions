class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        hasX = 0
        xMin = 101
        for x in nums:
            hasX |= 1 << x
            xMin = min(x, xMin)
        return -1 if xMin < k else (hasX.bit_count() +
                                    (-1 if xMin == k else 0))
