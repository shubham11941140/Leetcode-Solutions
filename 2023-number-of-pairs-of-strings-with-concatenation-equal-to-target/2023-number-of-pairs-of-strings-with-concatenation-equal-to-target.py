class Solution:

    def numOfPairs(self, nums: List[str], target: str) -> int:
        return len([
            1 for i in range(len(nums)) for j in range(len(nums))
            if i != j and nums[i] + nums[j] == target
        ])
