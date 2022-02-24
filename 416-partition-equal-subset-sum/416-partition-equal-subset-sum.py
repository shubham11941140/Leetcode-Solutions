class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # SOlve using DP 
        #Subset suim proble,
        n = len(nums)
        s = sum(nums)
        if s % 2:
            return False
        else:
            # Check if subset has sum s/2
            ns = s // 2
            dp = [[False for i in range(s + 1)] for j in range(n + 1)]
            dp[0][0] = True
            for i in range(1, n + 1):
                for j in range(1, s + 1):
                    if j >= nums[i - 1]:
                        dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
                    else:
                        dp[i][j] = dp[i - 1][j]
            for i in range(n + 1):
                if dp[i][ns]:
                    return True
            return False