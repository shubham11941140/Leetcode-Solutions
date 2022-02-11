class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        pre = [0] * n
        pre[0] = nums[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + nums[i]        
        if pre[n - 1] < target:
            return 0
        left = 0
        right = 0
        ans = n + 1
        while left < n and right < n and left <= right:
            while pre[right] < target:
                right += 1
            while pre[right] - pre[left] >= target:
                left += 1                
            diff = right - left + 1
            ans = min(ans, diff)
            right += 1
        return ans
            
        