class Solution:

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sums = [0] * (n + 1)
        for i in range(n):
            sums[i + 1] = sums[i] + nums[i]

        left = [0] * n
        total = sums[k] - sums[0]
        for i in range(k, n):
            if sums[i + 1] - sums[i + 1 - k] > total:
                total = sums[i + 1] - sums[i + 1 - k]
                left[i] = i + 1 - k
            else:
                left[i] = left[i - 1]

        right = [0] * n
        total = sums[n] - sums[n - k]
        right[n - k] = n - k
        for i in range(n - k - 1, -1, -1):
            if sums[i + k] - sums[i] >= total:
                total = sums[i + k] - sums[i]
                right[i] = i
            else:
                right[i] = right[i + 1]

        max_sum = 0
        result = [-1, -1, -1]
        for i in range(k, n - 2 * k + 1):
            l, r = left[i - 1], right[i + k]
            total = (
                (sums[i + k] - sums[i])
                + (sums[l + k] - sums[l])
                + (sums[r + k] - sums[r])
            )
            if total > max_sum:
                max_sum = total
                result = [l, i, r]

        return result
