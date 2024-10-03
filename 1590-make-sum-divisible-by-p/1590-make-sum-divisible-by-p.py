class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        remainder = total_sum % p
        if not remainder:
            return 0
        prefix_sum = 0
        min_length = len(nums)
        prefix_map = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            target = (prefix_sum - remainder + p) % p
            if target in prefix_map:
                min_length = min(min_length, i - prefix_map[target])
            prefix_map[prefix_sum] = i
        return min_length if min_length < len(nums) else -1
