class Solution:

    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        n = len(nums)
        return [i for i in d if d[i] > n // 3]
