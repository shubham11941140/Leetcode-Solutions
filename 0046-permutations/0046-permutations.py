class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            cur = nums[i]
            rem = nums[:i] + nums[i+1:]
            for x in self.permute(rem):
                res.append([cur] + x)
        return res        
        