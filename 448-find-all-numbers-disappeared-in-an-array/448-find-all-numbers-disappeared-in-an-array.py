class Solution:

    @staticmethod
    def findDisappearedNumbers(nums: List[int]) -> List[int]:
        h = set(sorted(list(set(nums))))
        return [i for i in range(1, len(nums) + 1) if i not in h]
