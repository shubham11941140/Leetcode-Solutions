class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()        
        n = len(nums)
        count = 0
        for i in range(n - 1):
            start = bisect.bisect_left(nums, lower - nums[i], i + 1, n)
            end = bisect.bisect_right(nums, upper - nums[i], i + 1, n) - 1
            if start <= end:
                count += end - start + 1        
        return count        