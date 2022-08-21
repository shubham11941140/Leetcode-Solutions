class Solution:

    @staticmethod
    def sortArrayByParity(nums: List[int]) -> List[int]:
        return [i for i in nums if i % 2 == 0] + [i for i in nums if i % 2]
