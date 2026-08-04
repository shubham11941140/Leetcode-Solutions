class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        l = [1] * n
        r = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    l[i] = max(l[i], l[j] + 1)
        for i in reversed(range(n - 1)):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    r[i] = max(r[i], r[j] + 1)
        return n - max(l[i] + r[i] - 1 for i in range(1, n - 1) if min(l[i], r[i]) > 1)
