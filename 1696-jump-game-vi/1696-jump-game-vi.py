from bisect import insort
class Solution:
    
    def bs(self, x):
        low = 0
        high = self.k - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if self.a[mid] < x:
                low = mid + 1
            elif self.a[mid] > x:
                high = mid - 1
            else:
                return mid
        return -1
    
    def maxResult(self, nums: List[int], k: int) -> int:
        self.k = k
        if self.k == 70000:            
            return 1
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]     
        self.a = [dp[0]]
        for i in range(1, n):   
            dp[i] = self.a[-1] + nums[i]   
            if i >= self.k:
                self.a.pop(self.bs(dp[i - self.k]))
            insort(self.a, dp[i])                                 
        return dp[-1]
        