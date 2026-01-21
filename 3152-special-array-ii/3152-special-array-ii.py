class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        parity = [num % 2 for num in nums]
        # Compute prefix sum of parity changes
        prefix_sum = [0] * (n + 1)
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + (parity[i] != parity[i - 1])
        return [prefix_sum[to] - prefix_sum[fro] == to - fro for fro, to in queries]
