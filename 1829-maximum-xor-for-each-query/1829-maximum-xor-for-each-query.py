class Solution:

    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (1 << maximumBit) - 1
        current_xor = 0
        result = []
        for num in nums:
            current_xor ^= num
        for i in range(len(nums)):
            result.append(current_xor ^ max_val)
            current_xor ^= nums[-(i + 1)]
        return result
