class Solution:

    @staticmethod
    def productExceptSelf(nums: List[int]) -> List[int]:
        if nums.count(0) > 1:
            return [0 for i in nums]
        if nums.count(0) == 1:
            m = 1
            for i in nums:
                if i:
                    m *= i
            a = [0 for i in range(len(nums))]
            for i, item in enumerate(nums):
                if not item:
                    a[i] = m
            return a
        m = 1
        for i in nums:
            m *= i
        return [m // i for i in nums]
