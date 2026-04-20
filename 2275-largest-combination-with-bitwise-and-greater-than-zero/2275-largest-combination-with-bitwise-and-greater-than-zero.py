class Solution:

    def largestCombination(self, candidates: List[int]) -> int:
        max_bits = max(candidates).bit_length()
        count = [0] * max_bits
        for num in candidates:
            for i in range(max_bits):
                if num & (1 << i):
                    count[i] += 1
        return max(count)
