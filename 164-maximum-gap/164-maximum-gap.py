class Solution:

    def maximumGap(self, nums: List[int]) -> int:
        a = sorted(list(set(nums)))
        if len(a) < 2:
            return 0
        return max([a[i + 1] - a[i] for i in range(len(a) - 1)])
