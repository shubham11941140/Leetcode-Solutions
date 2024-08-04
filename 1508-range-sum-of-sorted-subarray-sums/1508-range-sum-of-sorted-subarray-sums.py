class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # Initialize an array to store the sum of contiguous subarrays
        subarray_sums = []

        # Iterate through all possible subarrays
        for i in range(n):
            s = 0  # Initialize sum for subarray starting at index i
            for j in range(i, n):
                s += nums[j]  # Extend subarray and update sum
                subarray_sums.append(s)  # Add sum to the list

        # Sort the subarray sums
        subarray_sums.sort()

        # Return the sum of subarray_sums from left-1 to right-1
        return sum(subarray_sums[left - 1 : right]) % (10**9 + 7)
