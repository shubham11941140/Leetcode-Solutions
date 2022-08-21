class Solution:

    @staticmethod
    def maxCoins(nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0 for i in range(n)] for j in range(n)]
        for i in range(1, n + 1):
            for j in range(n - i):
                r = i + j
                m = [(dp[j][k] + dp[k][r] + nums[r] * nums[k] * nums[j])
                     for k in range(j + 1, r)]
                if m:
                    dp[j][r] = max(dp[j][r], max(m))
        return dp[0][n - 1]
