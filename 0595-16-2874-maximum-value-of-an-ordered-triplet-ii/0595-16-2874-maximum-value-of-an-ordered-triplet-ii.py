class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        l = [nums[0]] + [0] * (n - 1)
        for i in range(1, n):
            l[i] = max(l[i - 1], nums[i])
        r = [0] * (n - 1) + [nums[-1]]
        for i in range(n - 2, -1, -1):
            r[i] = max(r[i + 1], nums[i])
        return max([0] + [(l[i - 1] - nums[i]) * r[i + 1] for i in range(1, n - 1)])
