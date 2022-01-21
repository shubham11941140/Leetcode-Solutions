class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        print(n)
        # DP solution
        dp = [0 for i in range(n)]
        m = max(nums)
        print(m)
        
        for i in range(1, n):
            #for j in range(i): 
            # Put max condition optimization
            if i >= m + 10:
                check = [dp[j] for j in range(i - m - 10, i) if (i - j) <= nums[j]]
            else:
                check = [dp[j] for j in range(i) if (i - j) <= nums[j]]
            #print(check)
            #if not check:                break
            dp[i] = 1 + min(check)
        
        return dp[n - 1]

        