class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        l = [freq[num] + freq[num + 1] for num in freq if num + 1 in freq]
        return max(l) if l else 0