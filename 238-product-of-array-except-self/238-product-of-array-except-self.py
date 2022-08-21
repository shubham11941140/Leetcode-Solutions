class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in nums]
        elif nums.count(0) == 1:
            m = 1
            for i in nums:
                if i:
                    m *= i
            a = [0 for i in range(len(nums))]
            for i in range(len(nums)):
                if not nums[i]:
                    a[i] = m
            return a
        else:
            m = 1
            for i in nums:
                m *= i
            return [m // i for i in nums]
