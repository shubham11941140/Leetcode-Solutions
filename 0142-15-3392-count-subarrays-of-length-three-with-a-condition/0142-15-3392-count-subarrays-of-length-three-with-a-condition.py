class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        return len(
            [
                i
                for i in range(1, len(nums) - 1)
                if (nums[i - 1] + nums[i + 1]) * 2 == nums[i]
            ]
        )
