class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        num_sum = sum(nums)
        # Step 1: compute sum and F(0)
        F = sum([i * nums[i] for i in range(n)])
        maxVal = F
        # Step 2: use formula
        for k in range(1, n):
            F += num_sum - n * nums[n - k]
            maxVal = max(maxVal, F)
        return maxVal        