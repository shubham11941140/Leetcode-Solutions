class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Create a 2D array to store the maximum score difference between
        # player 1 and player 2 for the subarray starting at index i and
        # ending at index j
        dp = [[0] * len(nums) for _ in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for diagonal in range(1, len(nums)):
            for i in range(len(nums) - diagonal):
                j = i + diagonal
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0        