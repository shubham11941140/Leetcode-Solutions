class Solution:

    def numOfWays(self, nums: List[int]) -> int:

        def dfs(nums):
            if len(nums) <= 2:
                return 1
            left = [x for x in nums if x < nums[0]]
            right = [x for x in nums if x > nums[0]]
            return comb(len(left) + len(right),
                        len(right)) * dfs(left) * dfs(right)

        return (dfs(nums) - 1) % (10**9 + 7)
