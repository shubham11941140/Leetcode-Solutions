class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        queue = [(nums1[0] + nums2[i], 0, i) for i in range(min(k, len(nums2)))]
        heapify(queue)
        res = []
        while queue and len(res) < k:
            _, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])
            if i < len(nums1) - 1:
                heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
        return res        
           
        