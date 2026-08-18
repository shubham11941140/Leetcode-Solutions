class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)        
        subarray_count = {}        
        # Process all subarrays of size k
        for i in range(n - k + 1):
            for num in set(nums[i : i + k]):
                subarray_count[num] = subarray_count.get(num, 0) + 1
        
        # Find the largest integer that appears in exactly one subarray
        l = [num for num, count in subarray_count.items() if count == 1]
        return max(l) if l else -1