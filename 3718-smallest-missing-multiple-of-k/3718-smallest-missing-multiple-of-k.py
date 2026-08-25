class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        val = k
        i = 1
        while val in nums:
            val = k * i
            i += 1
        return val        