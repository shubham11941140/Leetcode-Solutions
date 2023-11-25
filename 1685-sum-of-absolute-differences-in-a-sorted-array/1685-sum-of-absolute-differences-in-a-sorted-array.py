class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        p = [0]
        for num in nums:
            p.append(p[-1] + num)
        total = p[-1]
        return [total - 2 * p[i] + num * (2 * i - len(nums)) for i, num in enumerate(nums)]      