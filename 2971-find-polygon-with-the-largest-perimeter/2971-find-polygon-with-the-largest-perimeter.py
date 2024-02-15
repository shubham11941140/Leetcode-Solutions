class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        p = [0 for i in range(n)]
        p[0] = nums[0]
        for i in range(1, n):
            p[i] = p[i - 1] + nums[i]
        s = 0
        for i in range(2, n):
            if p[i - 1] > nums[i]:
                s = p[i]
        return s if s else -1
            
        
        
        