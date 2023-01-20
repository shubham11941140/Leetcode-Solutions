class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        self.dfs(nums, 0, [], res)
        return res
    
    def dfs(self, nums, index, path, res):
        if len(path) > 1:
            res.add(tuple(path))
        for i in range(index, len(nums)):
            if not path or nums[i] >= path[-1]:
                self.dfs(nums, i + 1, path + [nums[i]], res)        