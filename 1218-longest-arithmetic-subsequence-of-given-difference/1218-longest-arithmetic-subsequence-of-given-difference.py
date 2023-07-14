class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = {}
        for i in arr:
            dp[i] = dp.get(i - difference, 0) + 1
        return max(dp.values())        