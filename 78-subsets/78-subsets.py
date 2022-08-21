class Solution:   

    def rec(self, nums, ans, idx,):        
        if idx == len(nums):
            self.f.append(ans)
            return
        self.rec(nums, ans + [nums[idx]], idx + 1) 
        self.rec(nums, ans, idx + 1)                   

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.f = []
        self.rec(nums, [], 0)      
        return self.f




