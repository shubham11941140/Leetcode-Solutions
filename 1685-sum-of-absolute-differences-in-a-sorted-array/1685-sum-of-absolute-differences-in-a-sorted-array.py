class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        total = prefix[-1]
        res = []
        for i, num in enumerate(nums):
            res.append(total - 2 * prefix[i] + num * (2 * i - len(nums)))
        return res
