class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if not n:
            return []
        if n == 1:
            return [nums]
        res = []
        for i in range(n):
            cur = nums[i]
            rem = nums[:i] + nums[i + 1:]
            for x in self.permute(rem):
                res.append([cur] + x)
        return res        
        