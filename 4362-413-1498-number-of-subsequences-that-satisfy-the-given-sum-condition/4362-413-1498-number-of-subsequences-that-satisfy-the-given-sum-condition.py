class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                ans += pow(2, r - l, 10 ** 9 + 7)
                l += 1
            else:
                r -= 1
        return ans % (10 ** 9 + 7)        