import numpy as np
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        sq = np.array(nums, dtype = np.int64) ** 2
        h = len(sq) // 2
        return int(sq.sum() - 2 * np.partition(sq, h)[:h].sum())