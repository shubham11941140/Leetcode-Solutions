class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        for i in range(n):
            pre[i] = pre[i - 1] + nums[i] if i else nums[i]             
        return pre