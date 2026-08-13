class Solution:

    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]
        if not nums:
            return 1
        m = min(nums)
        if m >= 2:
            return 1
        else:
            f = sorted(list(set(nums)))
            l = len(f)
            i = 0
            while i + 1 == f[i]:
                i += 1
                if i == l:
                    return l + 1
            return i + 1
