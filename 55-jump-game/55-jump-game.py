class Solution:

    @staticmethod
    def canJump(nums: List[int]) -> bool:
        n = len(nums)
        dp = [False for i in range(n)]
        dp[0] = True
        for i in range(1, n):
            for j in reversed(range(i)):
                if (i - j) <= nums[j] and dp[j]:
                    dp[i] = True
                    break
        return dp[n - 1]
