class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize with zero odd numbers (valid starting point)
        counter = Counter({0: 1})
        ans, t = 0, 0

        for v in nums:
            t += v & 1  # Check if v is odd
            ans += counter[t - k]  # Add count of valid subarrays
            # Update counter for the current count of odd numbers
            counter[t] += 1

        return ans
