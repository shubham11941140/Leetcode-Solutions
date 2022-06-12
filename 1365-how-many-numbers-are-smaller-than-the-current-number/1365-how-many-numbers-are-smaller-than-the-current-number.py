class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        return [len([j for j in range(n) if j != i and nums[j] < nums[i]]) for i in range(n)]
            
        