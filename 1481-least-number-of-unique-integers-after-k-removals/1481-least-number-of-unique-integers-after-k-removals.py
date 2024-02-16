class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        heap = [(freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        while k > 0:
            freq, num = heapq.heappop(heap)
            if freq <= k:
                k -= freq
            else:
                heapq.heappush(heap, (freq - k, num))
                k = 0

        return len(heap)
