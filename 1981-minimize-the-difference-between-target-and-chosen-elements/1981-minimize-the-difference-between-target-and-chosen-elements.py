class Solution:

    @staticmethod
    def minimizeTheDifference(mat: List[List[int]], target: int) -> int:
        n = len(mat)
        m = len(mat[0])
        s = sum([max(i) for i in mat])
        if n * m * s > 10**7:
            s = 2 * target
        dp = [[False for i in range(s + 1)] for j in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            b = list(set(mat[i - 1]))
            for k, item in enumerate(b):
                for j in range(1, s + 1):
                    if not dp[i][j] and j >= item:
                        dp[i][j] = dp[i - 1][j - item]
        ans = float("INF")
        for i in range(1, s + 1):
            if dp[n][i]:
                ans = min(ans, abs(target - i))
        if ans == float("INF"):
            return sum([min(i) for i in mat]) - target
        return ans
