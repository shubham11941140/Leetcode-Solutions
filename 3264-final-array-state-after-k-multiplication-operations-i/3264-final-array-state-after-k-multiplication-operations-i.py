class Solution:

    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            m = min(nums)
            nums[nums.index(m)] *= multiplier
        return nums
