from collections import Counter


class Solution:

    @staticmethod
    def majorityElement(nums: List[int]) -> List[int]:
        d = Counter(nums)
        n = len(nums)
        return [i for i in d if d[i] > n // 3]
