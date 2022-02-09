class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            h = list(set(nums))
            return len([i for i in h if nums.count(i) > 1])  
        nums = sorted(list(set(nums)))
        c = 0
        print(nums)
        for i in range(len(nums)):
            if nums[i] + k in nums:
                c += 1
            if nums[i] - k in nums:
                c += 1
        return c // 2
            
        nums.sort(reverse = True)
        n = len(nums)
        c = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) == k:
                    c += 1
        return c
        