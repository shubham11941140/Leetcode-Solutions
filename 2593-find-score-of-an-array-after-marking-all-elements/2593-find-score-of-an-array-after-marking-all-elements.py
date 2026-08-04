class Solution:

    def findScore(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        mp = {}
        # Min-heap to store (value, index) pairs
        pq = [(nums[i], i) for i in range(n)]
        heapify(pq)
        for _ in range(n):
            val, ind = heappop(pq)
            if ind not in mp:
                ans += val
                mp[ind] = True
                mp[ind - 1] = True
                mp[ind + 1] = True
        return ans
