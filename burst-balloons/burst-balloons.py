class Solution:

    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n + 1):
            for j in range(n - i):
                r = i + j
                for k in range(j + 1, r):
                    dp[j][r] = max(
                        dp[j][r],
                        dp[j][k] + dp[k][r] + nums[r] * nums[k] * nums[j])
        return dp[0][n - 1]
