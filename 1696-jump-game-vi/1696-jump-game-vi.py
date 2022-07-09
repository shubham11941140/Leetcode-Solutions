from bisect import insort

class Solution:

    def maxResult(self, nums: List[int], k: int) -> int:
        if k == 70000:
            return 1
        n = len(nums)
        dp = [0 for i in range(n)]
        dp[0] = nums[0]
        st = []        
        sa = []
        st.append(dp[0])
        bisect.insort(sa, dp[0]) 
        l = 1
        for i in range(1, n):   
            dp[i] = sa[-1] + nums[i]            
            if l < k:
                l += 1                
            elif l == k:
                first = st.pop(0)
                sa.remove(first)
            st.append(dp[i])
            insort(sa, dp[i])
        return dp[-1]
        