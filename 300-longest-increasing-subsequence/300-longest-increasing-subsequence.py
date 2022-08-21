from bisect import bisect_left
class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        t = [0 for i in range(n + 1)]
        l = 1
        t[0] = nums[0]
        for i in range(1, n):
            if nums[i] > t[l - 1]:
                t[l] = nums[i]
                l += 1
            else:
                t[bisect_left(t, nums[i], 0, l - 1)] = nums[i]
        return l      
                
        
