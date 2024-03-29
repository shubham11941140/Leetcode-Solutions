class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:            
            curr = nums[i]
            while i < n - 1 and nums[i + 1] == nums[i] + 1:                
                i += 1
            ans.append(str(curr) if curr == nums[i] else str(curr) + "->" + str(nums[i])) 
            i += 1
        return ans
        