class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        n = len(profits)
        arr = sorted(zip(capital, profits), key=lambda x: x[0])
        i = 0
        heap = []
        while k:
            while i < n and arr[i][0] <= w:
                heapq.heappush(heap, -arr[i][1])
                i += 1
            if heap:
                w -= heapq.heappop(heap)
            k -= 1
        return w
