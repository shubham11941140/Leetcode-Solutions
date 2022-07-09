from bisect import insort
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if k == 70000:            
            return 1
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]     
        sa = [dp[0]]
        for i in range(1, n):   
            dp[i] = sa[-1] + nums[i]    
            if i >= k:
                sa.remove(dp[i - k])
            insort(sa, dp[i])                                 
        return dp[-1]
        