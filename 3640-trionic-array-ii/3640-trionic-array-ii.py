class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        result = float('-inf')
        preSum = nums[0]
        l = 0
        p = 0
        q = 0
        for r in range(1, n):
            preSum += nums[r]
            if nums[r - 1] == nums[r]:
                l = r
                preSum = nums[r]
            elif nums[r - 1] > nums[r]:  # this r-1 might be a peak
                if r > 1 and nums[r - 2] < nums[r - 1]:
                    p = r - 1  # yes, we found one local peak (marked it)
                    while l < q:
                        preSum -= nums[l]
                        l += 1
                    while l < p - 1 and nums[l] < 0:
                        preSum -= nums[l]
                        l += 1
            else:
                if r > 1 and nums[r - 2] > nums[r - 1]:
                    q = r - 1  # found valley point
                if l < p < q:
                    result = max(result, preSum)
        return result        