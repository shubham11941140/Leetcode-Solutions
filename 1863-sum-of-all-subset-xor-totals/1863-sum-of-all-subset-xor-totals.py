class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def xor(binary_string):
            total = 0
            for i, char in enumerate(binary_string):
                if char == '1':
                    total = total ^ nums[i]
            return total
            # (not a and b) or (not b and a)

        total = 0

        for i in range(1, 1 << len(nums)):
            total += xor(bin(i)[2:].zfill(len(nums)))
            
        return total      