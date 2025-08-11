class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        lengths = [1] * n
        counts = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        max_length = max(lengths)
        result = sum(
            count for length, count in zip(lengths, counts) if length == max_length
        )
        return result
