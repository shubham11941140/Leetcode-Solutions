from collections import Counter

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        f = Counter(nums)
        return [i for i in f if f[i] == 1][0]
        
