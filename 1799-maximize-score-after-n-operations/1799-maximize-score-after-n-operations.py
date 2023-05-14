class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def dp(mask, i):
            if i == len(nums) // 2:
                return 0
            res = 0
            for j in range(len(nums)):
                if mask & (1 << j):
                    continue
                for k in range(j + 1, len(nums)):
                    if mask & (1 << k):
                        continue
                    res = max(res, (i + 1) * gcd(nums[j], nums[k]) + dp(mask | (1 << j) | (1 << k), i + 1))
            return res

        return dp(0, 0)