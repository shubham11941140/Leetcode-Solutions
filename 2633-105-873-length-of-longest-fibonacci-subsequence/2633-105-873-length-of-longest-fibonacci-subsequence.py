class Solution:

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        # Map each number to its index
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_len = 0

        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:  # Check if a valid Fibonacci sequence exists
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[j, k])

        # Return 0 if no Fibonacci-like subsequence exists
        return max_len if max_len >= 3 else 0
