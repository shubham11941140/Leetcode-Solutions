class Solution:

    @staticmethod
    def combinationSum4(nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = [0 for i in range(target + 1)]
        for i in nums:
            if i > target:
                break
            dp[i] = 1
        for i in range(target + 1):
            for j in nums:
                if j > i:
                    break
                dp[i] += dp[i - j]
        return dp[target]
