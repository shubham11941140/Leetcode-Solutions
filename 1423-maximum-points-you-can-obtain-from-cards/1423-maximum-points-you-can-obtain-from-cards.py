class Solution:

    def maxScore(self, cardPoints: List[int], k: int) -> int:
        a = cardPoints.copy()
        b = a[::-1]
        n = len(a)
        ans = 0
        pre = [0] * n
        rpre = [0] * n
        pre[0] = a[0]
        rpre[0] = b[0]
        for i in range(1, n):
            pre[i] = pre[i - 1] + a[i]
            rpre[i] = rpre[i - 1] + b[i]
        for i in range(k + 1):
            if 0 <= i - 1 < n and 0 <= k - i - 1 < n:
                val = pre[i - 1] + rpre[k - i - 1]
            elif 0 <= i - 1 < n and not 0 <= k - i - 1 < n:
                val = pre[i - 1]
            elif not (0 <= i - 1 < n) and 0 <= k - i - 1 < n:
                val = rpre[k - i - 1]
            ans = max(ans, val)
        return ans
