class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c = Counter(nums)
        m = max(c.values())
        return sum([m for i in c if c[i] == m])
