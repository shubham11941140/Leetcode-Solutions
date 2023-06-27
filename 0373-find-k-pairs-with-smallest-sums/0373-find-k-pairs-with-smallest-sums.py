class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        queue = [(nums1[0] + nums2[i], 0, i) for i in range(min(k, len(nums2)))]
        heapq.heapify(queue)
        res = []
        while queue and len(res) < k:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            if i + 1 < len(nums1):
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
        return res        
        
        
        
        
        
        maxheap = []
        for i in range(min(k // 2, len(nums1))):
            for j in range(min(k // 2, len(nums2))):
                s = 0
                s += nums1[i] + nums2[j]
                heappush(maxheap, [-s, [nums1[i],nums2[j]]])
                if len(maxheap) > k:
                    heappop(maxheap)
        res = []
        while maxheap:
            _, i = heappop(maxheap)
            res.append(i)
        return res[::-1]
            
        