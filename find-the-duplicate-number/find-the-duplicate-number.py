from collections import Counter


class Solution:

    @staticmethod
    def findDuplicate(nums: List[int]) -> int:
        f = Counter(nums)
        for i in f:
            if f[i] > 1:
                return i
