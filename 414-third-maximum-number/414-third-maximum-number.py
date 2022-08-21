class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = set(nums)
        if len(s) > 2:            
            return sorted(list(s))[-3]
        return max(s)
        