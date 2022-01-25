from collections import Counter

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = Counter(nums)
        return sum([i for i in d if d[i] == 1])
        