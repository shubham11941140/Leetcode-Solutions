class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # First, we sort the list of numbers in ascending order.
        nums.sort()

        # The largest elements will be at the end of the sorted list, and
        # the smallest elements will be at the beginning.
        # Therefore, the product of the two largest elements can be found
        # by multiplying the last two elements in the sorted list.
        largest_product = nums[-1] * nums[-2]

        # Similarly, the product of the two smallest elements can be found
        # by multiplying the first two elements in the sorted list.
        smallest_product = nums[0] * nums[1]

        # The maximum product difference is the difference between the
        # largest product and the smallest product.
        max_product_difference = largest_product - smallest_product

        # Return the computed maximum product difference.
        return max_product_difference
