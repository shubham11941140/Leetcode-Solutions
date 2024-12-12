class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-pile for pile in gifts]
        heapify(max_heap)
        for _ in range(k):
            heappush(max_heap, -floor(sqrt(-heappop(max_heap))))
        return -sum(max_heap)