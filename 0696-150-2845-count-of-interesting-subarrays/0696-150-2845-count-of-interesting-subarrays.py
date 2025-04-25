class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_count = Counter({0: 1})  # Initialize with prefix sum 0
        p = 0
        result = 0
        for num in nums:
            # Update prefix sum based on the condition
            p = (p + (num % modulo == k)) % modulo
            # Count subarrays ending at the current index
            result += prefix_count[(p - k + modulo) % modulo]
            # Update prefix count
            prefix_count[p] += 1
        return result        