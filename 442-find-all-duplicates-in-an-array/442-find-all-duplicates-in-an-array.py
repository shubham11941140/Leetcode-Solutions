from collections import Counter


class Solution:

    @staticmethod
    def findDuplicates(nums: List[int]) -> List[int]:
        d = Counter(nums)
        return [i for i in d if d[i] == 2]
