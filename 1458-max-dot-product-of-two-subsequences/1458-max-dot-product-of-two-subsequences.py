class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[float("-inf")] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = max(
                    dp[i][j] + nums1[i] * nums2[j],
                    nums1[i] * nums2[j],
                    dp[i + 1][j],
                    dp[i][j + 1],
                )
        return dp[-1][-1]
