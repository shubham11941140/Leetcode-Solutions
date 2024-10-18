class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        def dfs(i, current_or):
            if i == len(nums):
                return 1 if current_or == max_or else 0
            return dfs(i + 1, current_or | nums[i]) + dfs(i + 1, current_or)

        return dfs(0, 0)

        