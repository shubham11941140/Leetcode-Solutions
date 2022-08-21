from collections import Counter


class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        return [i for i in d if d[i] == 2]
