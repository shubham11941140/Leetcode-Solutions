class Solution:
    
    def remneg(self, a):
        return [i for i in a if i > 0]
    
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = self.remneg(nums)
        if not nums:
            return 1
        m = min(nums)
        if m >= 2:
            return 1
        f = sorted(list(set(nums)))
        l = len(f)
        i = 0
        #print(f)
        while i + 1 == f[i]:
            i += 1
            if i == l:
                return l + 1
        return i + 1
        