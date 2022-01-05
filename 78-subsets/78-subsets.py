class Solution:   
       
    def rec(self, nums, ans, idx, final):        
        if idx == len(nums):
            final.append(ans)
            return
        self.rec(nums, ans + [nums[idx]], idx + 1, final) 
        self.rec(nums, ans, idx + 1, final)                   
                
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        self.rec(nums, [], 0, final)      
        return final
        
        
        
        