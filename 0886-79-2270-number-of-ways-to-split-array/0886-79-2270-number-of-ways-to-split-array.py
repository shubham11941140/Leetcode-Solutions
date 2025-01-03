class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]        
        # Calculate the prefix sum array
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]        
        total_sum = prefix_sum[-1]
        count = 0        
        # Iterate through the array to find the valid splits
        for i in range(n - 1):
            left_sum = prefix_sum[i]
            right_sum = total_sum - left_sum
            if left_sum >= right_sum:
                count += 1        
        return count   