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

                # Player 1 can either choose the number at index i or index j
                # If they choose the number at index i, then player 2 will play optimally
                # and take the maximum score difference for the subarray starting at index i+1 and ending at j
                # Player 1 will then be left with the subarray starting at index i+2 and ending at j, where they
                # can choose either the number at index i+2 or index j
                # If they choose the number at index j, then player 2 will play optimally
                # and take the maximum score difference for the subarray starting at index i and ending at j-1
                # Player 1 will then be left with the subarray starting at index i+1 and ending at j-1, where they
                # can choose either the number at index i+1 or index j-1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

        # If the maximum score difference for the subarray starting at index 0
        # and ending at the last index is greater than or equal to 0, then player 1 can win
        return dp[0][-1] >= 0        