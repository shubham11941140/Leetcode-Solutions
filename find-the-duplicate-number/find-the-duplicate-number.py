from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f = Counter(nums)
        for i in f:
            if f[i] > 1:
                return i
        