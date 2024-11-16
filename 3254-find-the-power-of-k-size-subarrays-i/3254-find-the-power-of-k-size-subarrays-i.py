class Solution:
    
    def check(self, a):
        if max(a) - min(a) + 1 != len(a):
            return -1
        return a[-1] if a == [i for i in range(min(a), max(a) + 1)] else -1
    
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        return [self.check(nums[i:i + k]) for i in range(len(nums) - k + 1)]        