class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # Create a 2D array to store the maximum score difference between
        # player 1 and player 2 for the subarray starting at index i and
        # ending at index j
        dp = [[0] * len(nums) for _ in range(len(nums))]

        # Fill the diagonal with the values of the array, as the subarray
        # starting and ending at the same index will only contain one number
        for i in range(len(nums)):
            dp[i][i] = nums[i]

        # Iterate through the array and fill the remaining cells in the 2D array
        # We start at the second diagonal and work our way up
        for diagonal in range(1, len(nums)):
            for i in range(len(nums) - diagonal):
                j = i + diagonal
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0        