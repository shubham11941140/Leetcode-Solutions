class Solution:

    def tupleSameProduct(self, nums: List[int]) -> int:
        product_pairs = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                product = nums[i] * nums[j]
                count += product_pairs[product]
                product_pairs[product] += 1
        # Each tuple (i, j, k, l) contributes 8 combinations of (i, j, k, l)
        return count * 8
