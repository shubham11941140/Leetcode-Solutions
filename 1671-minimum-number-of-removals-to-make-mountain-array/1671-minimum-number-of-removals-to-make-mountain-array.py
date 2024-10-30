class Solution:

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        # Calculate the longest increasing subsequence ending at each index
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)

        # Calculate the longest decreasing subsequence starting at each index
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)

        # Find the maximum length of mountain array
        max_length = 0
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                max_length = max(max_length, left[i] + right[i] - 1)

        return n - max_length
