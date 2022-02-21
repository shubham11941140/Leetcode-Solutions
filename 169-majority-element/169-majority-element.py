from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = Counter(nums)
        n = len(nums)
        return [i for i in d if d[i] > n // 2][0]
        