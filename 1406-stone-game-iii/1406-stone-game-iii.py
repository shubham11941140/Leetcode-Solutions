class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)
        for i in reversed(range(n)):
            take = 0
            dp[i] = float('-inf')
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