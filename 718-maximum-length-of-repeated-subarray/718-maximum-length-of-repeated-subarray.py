class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for i in range(n2)] for j in range(n1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    else:
                        dp[i][j] = 1
        return max([max(i) for i in dp])   