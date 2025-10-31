class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v == 2]