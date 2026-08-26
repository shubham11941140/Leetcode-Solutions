class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p = [0]
        for i in nums:
            p.append(p[-1] + i)
        return [
            p[-1] - 2 * p[i] + num * (2 * i - len(nums))
            for i, num in enumerate(nums)
        ]
