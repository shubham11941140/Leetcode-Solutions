class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)  # dp[i] represents the maximum score difference starting from index i

        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = float('-inf')  # Initialize dp[i] to negative infinity

            # Try taking 1, 2, or 3 stones and calculate the maximum score difference
            for j in range(3):
                if i + j < n:
                    take += stoneValue[i + j]
                    dp[i] = max(dp[i], take - dp[i + j + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"      