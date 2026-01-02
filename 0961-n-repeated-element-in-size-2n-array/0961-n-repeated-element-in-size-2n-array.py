class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v > 1][0]