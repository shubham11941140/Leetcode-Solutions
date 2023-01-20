class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.r = set()
        self.nums = nums.copy()
        self.n = len(nums)
        self.dfs(0, [])
        return self.r

    def dfs(self, index, path):
        if len(path) > 1:
            self.r.add(tuple(path))
        for i in range(index, self.n):
            if not path or self.nums[i] >= path[-1]:
                self.dfs(i + 1, path + [self.nums[i]])        