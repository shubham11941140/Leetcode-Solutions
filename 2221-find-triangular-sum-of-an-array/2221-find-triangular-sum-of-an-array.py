class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n1 = len(nums)
        for _ in range(n1 - 1):
            nums = [(nums[i] + nums[i + 1]) % 10 for i in range(len(nums) - 1)]
        return nums[0]
                
        