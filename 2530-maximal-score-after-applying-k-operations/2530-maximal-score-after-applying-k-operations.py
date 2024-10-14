class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        return heapify(h := [*map(neg, nums)]) or -sum(heappushpop(h, h[0] // 3) for _ in range(k))