class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [{} for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = (dp[j][d] + 1 if d in dp[j] else 2)
                res = max(res, dp[i][d])
        return res
       