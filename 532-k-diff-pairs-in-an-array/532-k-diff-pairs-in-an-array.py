class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            h = list(set(nums))
            return len([i for i in h if nums.count(i) > 1])  
        nums = sorted(list(set(nums)))
        c = 0
        for i, item in enumerate(nums):
            if item + k in nums:
                c += 1
            if item - k in nums:
                c += 1
        return c // 2
        