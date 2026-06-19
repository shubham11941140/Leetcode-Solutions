class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        for i in range(len(nums)):
            x = heappop(nums)
            if x < k:
                res += 1
                y = heappop(nums)
                val = x * 2 + y if x < y else y * 2 + x
                heappush(nums, val)
            else:
                break
        return res
