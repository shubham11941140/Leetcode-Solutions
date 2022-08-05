class Solution:
    
    def rec(self, target):
        if not target:
            self.ans += 1
        for i in self.nums:
            if i > target:
                break                
            self.rec(target - i)
    
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.nums = sorted(nums)
        self.ans = 0
        #self.rec(target)
        n = len(nums)
        
        dp = [0 for i in range(target + 1)]
        for i in nums:
            if i <= target:
                dp[i] = 1
        
        for i in range(target + 1):
            for j in range(n):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
        print(dp)
        return dp[target]
        
        return self.ans
        