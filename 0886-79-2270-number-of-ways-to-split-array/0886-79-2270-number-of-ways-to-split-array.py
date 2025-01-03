class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]        
        # Calculate the prefix sum array
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]        
        return len([i for i in range(n - 1) if 2 * prefix_sum[i] >= prefix_sum[-1]])  