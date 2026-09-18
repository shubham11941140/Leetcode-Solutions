class Solution:

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        n = len(nums)
        for num in nums:
            max_or |= num
        def dfs(i, current_or):
            if i == n:
                return int(current_or == max_or)
            return dfs(i + 1, current_or | nums[i]) + dfs(i + 1, current_or)
        return dfs(0, 0)
