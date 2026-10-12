class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        cnt = [sum(x >> b & 1 for x in nums) for b in range(30)]
        return sum([sum(1 << b for b in range(30) if cnt[b] > i) ** 2 for i in range(k)]) % (10 ** 9 + 7)