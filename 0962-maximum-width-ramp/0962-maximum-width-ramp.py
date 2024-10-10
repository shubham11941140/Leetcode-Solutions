class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:        
        stack = []
        max_width = 0
        n = len(nums)
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        for j in reversed(range(n)):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())        
        return max_width        