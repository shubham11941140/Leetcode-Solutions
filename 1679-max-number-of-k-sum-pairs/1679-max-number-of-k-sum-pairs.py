from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        return sum([min(f[i], f[k - i]) for i in f if k - i in f]) // 2

