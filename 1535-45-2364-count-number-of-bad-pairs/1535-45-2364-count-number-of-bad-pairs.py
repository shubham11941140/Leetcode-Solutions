class Solution:

    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        total_pairs = 0
        good_pairs = 0
        for i, num in enumerate(nums):
            diff = i - num
            total_pairs += i
            good_pairs += freq[diff]
            freq[diff] += 1
        return total_pairs - good_pairs
