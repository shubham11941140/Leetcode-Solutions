class Solution:

    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        for i in range(n):
            s = 0  # Initialize sum for subarray starting at index i
            for j in range(i, n):
                s += nums[j]  # Extend subarray and update sum
                subarray_sums.append(s)  # Add sum to the list
        return sum(sorted(subarray_sums)[left - 1 : right]) % (10**9 + 7)
