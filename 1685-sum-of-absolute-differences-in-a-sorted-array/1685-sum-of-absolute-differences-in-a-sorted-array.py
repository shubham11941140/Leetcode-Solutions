class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        total = prefix[-1]
        return [
            total - 2 * prefix[i] + num * (2 * i - len(nums))
            for i, num in enumerate(nums)
        ]
