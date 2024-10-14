class Solution:

    def maxKelements(self, nums: List[int], k: int) -> int:
        a = nums.copy()
        return heapify(h := [*map(neg, a)]) or -sum(
            heappushpop(h, h[0] // 3) for _ in range(k)
        )
        max_heap = [-num for num in nums]
        heapify(max_heap)
        score = 0
        for _ in range(k):
            largest = -heappop(max_heap)
            score += largest
            heappush(max_heap, ceil(largest / 3))
        return score
