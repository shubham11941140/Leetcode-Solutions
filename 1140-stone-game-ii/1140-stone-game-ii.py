class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        memo = {}

        def dp(start, M):
            if (start, M) in memo:
                return memo[(start, M)]

            if start + 2 * M >= n:
                return suffix_sum[start]

            res = float('-inf')
            for i in range(1, 2 * M + 1):
                res = max(res, suffix_sum[start] - dp(start + i, max(i, M)))
            memo[(start, M)] = res
            return res

        return dp(0, 1)

        