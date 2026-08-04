class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum = 0
        count = defaultdict(int)  # Store the count of prefix sums
        total_subarrays = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum == goal:
                total_subarrays += 1
            total_subarrays += count[prefix_sum - goal]
            count[prefix_sum] += 1
        return total_subarrays
