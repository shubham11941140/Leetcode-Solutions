class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for i in range(n)]
        m = max(nums)       
        for i in range(1, n):
            if i >= m + 10:
                check = [dp[j] for j in range(i - m - 10, i) if (i - j) <= nums[j]]
            else:
                check = [dp[j] for j in range(i) if (i - j) <= nums[j]]
            dp[i] = 1 + min(check)        
        return dp[n - 1]

        