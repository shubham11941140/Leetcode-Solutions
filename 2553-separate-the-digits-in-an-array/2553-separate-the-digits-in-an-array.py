class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a = []
        for j in nums:
            a += [int(i) for i in str(j)]
        return a        