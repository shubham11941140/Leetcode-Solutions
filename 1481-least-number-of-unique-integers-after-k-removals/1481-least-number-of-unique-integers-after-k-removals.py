class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        heap = [(freq, num) for num, freq in count.items()]
        heapify(heap)
        while k > 0:
            freq, num = heappop(heap)
            if freq <= k:
                k -= freq
            else:
                heappush(heap, (freq - k, num))
                k = 0
        return len(heap)        