class Solution:
    def missingNumber(self, nums: List[int]) -> int:        
        n = len(nums)
        a = [0] * (n + 1)        
        for i in range(n):
            a[nums[i]] += 1
        for i in range(n + 1):
            if not a[i]:
                return i