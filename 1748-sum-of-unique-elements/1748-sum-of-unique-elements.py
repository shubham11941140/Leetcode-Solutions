from collections import Counter


class Solution:

    @staticmethod
    def sumOfUnique(nums: List[int]) -> int:
        d = Counter(nums)
        return sum([i for i in d if d[i] == 1])
